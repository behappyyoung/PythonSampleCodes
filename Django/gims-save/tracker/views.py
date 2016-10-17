from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.core import serializers
from .models import Samples, Orders, SampleOrderRel, Patients, PhenoTypes, OrderPhenoTypes, PatientOrderPhenoType, PatientOrderPhenoList, OrderGeneList
from .forms import OrderForm, OrderGeneListForm
from mybackend.models import CustomSQL, PhenoTypeLists, GeneLists
from mybackend import functions, LoadOntology
from logger.models import accessLog, loomLog, logging
import json
from gims import settings
from django.contrib import messages
from .forms import SampleOrderRelForm, PatientOrderPhenoTypeForm, PhenoTypesForm, GeneListsForm
from datetime import datetime
from django.core.cache import cache

def custom_proc(request):
    return {
        'LOOMURL': settings.LOOMURL,
    }

BASE_SAMPLE_SQL = 'SELECT s.*,  o.id as order_id, o.order_name, rt.rel_name as relation, ot.type_name as order_type FROM tracker_samples s ' \
                  ' left join tracker_sampleorderrel r on s.id = r.sample_id left join tracker_orders o on r.order_id = o.id ' \
                  ' left join tracker_relations rt on r.relation_id = rt.id left join tracker_ordertype ot on o.type_id = ot.id'

BASE_SAMPLEFILES_SQL='SELECT sf.*, s.asn as asn, o.order_name as ordername from tracker_samplefiles sf join tracker_samples s on sf.sample_id = s.id join tracker_orders o on sf.order_id = o.id'


@login_required(login_url='/login/')
def samples_view(request):
    if 'username' in request.session:
        print(request.session.get('username'), request.session['username'])
    else:
        return HttpResponseRedirect('/saml/?slo')
    myc = CustomSQL()
    c_samples = myc.my_custom_sql(BASE_SAMPLE_SQL +' order by s.asn; ')
    logging(request, 'access')
    return render(request, 'tracker/samples.html', {'samples':json.dumps(c_samples)})


SAMPLE_WORKFLOWS_SQL = 'SELECT * from tracker_samples s join logger_loomlog l on s.asn = l.relSample '


@login_required(login_url='/login/')
def sample_details(request, sid):
    if 'username' in request.session:
        print(request.session.get('username'), request.session['username'])
    else:
        return HttpResponseRedirect('/saml/?slo')
    myc = CustomSQL()
    c_samples = myc.my_custom_sql(BASE_SAMPLE_SQL + ' WHERE s.id = "' + sid + '" order by s.asn; ')
    asn = c_samples[0]['asn']
    c_samplefiles = myc.my_custom_sql(BASE_SAMPLEFILES_SQL  + ' WHERE s.id = "' + sid + '" ')

    c_loomlog = loomLog.objects.using('logs').filter(relSample = asn)
    jsonstring_loomlog = serializers.serialize('json', c_loomlog, fields=('analysisID', 'workflowID', 'relOrder', 'acc_time', 'loomResponse'))
    logging(request, 'access')
    return render(request, 'tracker/sample_details.html',
                  {'samples':json.dumps(c_samples), 'samplesfiles': json.dumps(c_samplefiles), 'workflows': jsonstring_loomlog},
                  context_instance=RequestContext(request, processors=[custom_proc]))


BASE_ORDER_SQL = 'SELECT *, o.id as orderid FROM tracker_orders o  left join tracker_sampleorderrel rel ' \
                 'on o.id = rel.order_id  left join tracker_samples s on rel.sample_id = s.id ' \
                 'left join tracker_relations rt on rel.relation_id = rt.id' \
                ' left join tracker_ordertype ot on o.type_id = ot.id ' \
                'left join tracker_orderstatus os on o.status_id = os.id'


SIMPLE_ORDER_SQL = 'SELECT *, o.id as order_id FROM tracker_orders o ' \
                ' left join tracker_ordertype ot on o.type_id = ot.id ' \
                'left join tracker_orderstatus os on o.status_id = os.id'


@login_required(login_url='/saml/')
def orders_view(request):
    if 'username' in request.session:
        print(request.session.get('username'), request.session['username'])
    else:
        return HttpResponseRedirect('/saml/?slo')
    myc = CustomSQL()
    mysql = SIMPLE_ORDER_SQL+'  order by o.due_date; '
    c_orders = myc.my_custom_sql(mysql)            # raw dict
    logging(request, 'access')
    return render(request, 'tracker/orders.html', {'orders':json.dumps(c_orders)})


@login_required(login_url='/saml/')
def order_details(request, oid):
    if 'username' in request.session:
        print(request.session.get('username'), request.session['username'])
    else:
        return HttpResponseRedirect('/saml/?slo')
    myc = CustomSQL()
    c_orders = myc.my_custom_sql(BASE_ORDER_SQL+' WHERE o.id = "' + oid + '" order by o.due_date; ')            # raw dict
    oname = c_orders[0]['order_name']
    phenolists = PhenoTypeLists.objects.select_related('category').all().order_by('mybackend_phenotypecategory.priority', 'priority', 'name')
    try:
        c_phenolist = OrderPhenoTypes.objects.filter(order_id=oid)
        jsonstring_phenolist = serializers.serialize('json', c_phenolist)
    except OrderPhenoTypes.DoesNotExist:
        jsonstring_phenolist = []
    try:
        genelist = OrderGeneList.objects.select_related('genelist').filter(order_id=oid)
    except OrderGeneList.DoesNotExist:
        print ('no genelist')
    c_loomlog = loomLog.objects.using('logs').filter(relOrder=oname)
    jsonstring_loomlog = serializers.serialize('json', c_loomlog,
                                               fields=('analysisID', 'workflowID', 'relSample', 'acc_time', 'loomResponse'))
    logging(request, 'access')
    return render(request, 'tracker/order_details.html',
                  {'orders':json.dumps(c_orders), 'phenolists' : c_phenolist, 'workflows': jsonstring_loomlog, 'genelists':genelist},
                  context_instance=RequestContext(request, processors=[custom_proc]))


@login_required(login_url='/saml/')
def order_new(request):
    form = OrderForm(request.POST)
    if form.is_valid():
        form.save()

    else:
        form = OrderForm()

    return render(request, 'tracker/order_new.html', {'form' : form})


@login_required(login_url='/saml/')
def patients(request):
    if 'username' in request.session:
        print(request.session.get('username'), request.session['username'])
        if 'Interpretation' not in request.session.get('role') and 'Manager' not in request.session.get('role'):
            message = " You do not have permission to load  %s" % request.path_info
            messages.error(request, message)
            logging(request, 'UnAuthorized')
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/saml/?slo')
    c_patients = Patients.objects.all()
    jsonstring_patients = serializers.serialize('json', c_patients)
    logging(request, 'access')
    return render(request, 'tracker/patients.html', {'patients':jsonstring_patients})


# patient details page
@login_required(login_url='/saml/')
def patient_details(request, pid):
    if 'username' in request.session:
        if 'interpretation' not in request.session.get('role').lower() and 'manager' not in request.session.get(
                'role').lower():
            message = " You do not have permission to load  %s" % request.path_info
            messages.error(request, message)
            logging(request, 'UnAuthorized')
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/saml/?slo')
    patient = Patients.objects.get(pid=pid)
    samples = Samples.objects.filter(patient_id=pid).order_by('asn')
    orders = Orders.objects.filter(patient_id=pid)
    oids=[]
    for order in orders:
        oids.append(int(order.id))

    if len(oids)>0:
        phenotypes = OrderPhenoTypes.objects.filter(order_id__in=oids)
    else:
        phenotypes =[]
    logging(request, 'access')
    return render(request, 'tracker/patient_details.html',
                  {'patient':patient, 'samples':samples, 'phenotypes': phenotypes,'orders':orders})


@login_required(login_url='/saml/')
def add_SampleOrderRel(request):
    if request.method == 'POST':
        form = SampleOrderRelForm(request.POST)
        if form.is_valid():
            if request.POST['action'] == 'delete':
                sor = SampleOrderRel.objects.get(order_id=request.POST['order'], sample_id=request.POST['sample'], relation_id=request.POST['relation'])
                sor.delete()
            elif request.POST['action'] == 'edit':
                sor = SampleOrderRel.objects.get(order_id=request.POST['order'], sample_id=request.POST['sample'])
                sor.relation_id = request.POST['relation']
                sor.save()
            else:           # add

                if SampleOrderRel.objects.filter(order_id=request.POST['order'], sample_id=request.POST['sample']).exists():
                    return render(request, 'tracker/SampleOrderRel.html',
                                  {'form': form, 'action': request.POST['action'], 'message':' Record Exists - do you want to update ?'})
                else:
                    form.save()
            return HttpResponseRedirect('/order/'+request.POST['order']+'/')

        return render(request, 'tracker/SampleOrderRel.html', {'form': form, 'action': request.POST['action']})
    else:

        if not request.META['QUERY_STRING']:
            form = SampleOrderRelForm()
            action = 'add'
        else:
            oid = request.GET.get('oid')
            sid = request.GET.get('sid')
            rid = request.GET.get('rid')
            try:
                sor = SampleOrderRel.objects.get(order_id=oid, sample_id=sid, relation_id=rid)
                form = SampleOrderRelForm(instance=sor)
                action = 'edit'
            except SampleOrderRel.MultipleObjectsReturned:
                form = SampleOrderRelForm(initial={'order': oid, 'sample': sid, 'relation': rid})
                action = 'edit'
            except SampleOrderRel.DoesNotExist:
                form = SampleOrderRelForm(initial={'order': oid, 'sample': sid, 'relation': rid})
                action = 'add'
    logging(request, 'access')
    return render(request, 'tracker/SampleOrderRel.html', {'form': form, 'action':action })


@login_required(login_url='/saml/')
def add_patient_order_phenopype(request, oid):
    if request.method == 'POST':

        try:
            c_phenolist = PatientOrderPhenoList.objects.get(order_id=oid)
            c_phenolist.pheno_checklists = request.POST['checkList']
            c_phenolist.pheno_valuelists = request.POST['textInput']
            c_phenolist.save()


        except PatientOrderPhenoList.DoesNotExist:
            c_phenolist = PatientOrderPhenoList(order_id = oid, pheno_checklists = request.POST['checkList'], pheno_valuelists = request.POST['textInput'])
            c_phenolist.save()

        return HttpResponse(json.dumps({'reURL':'/order/'+oid+'/'}))
    else:
        try:
            c_phenolist = PatientOrderPhenoList.objects.get(order_id=oid)
            c_list = {'checkInput':str(c_phenolist.pheno_checklists), 'textInput' : str(c_phenolist.pheno_valuelists)}
            action = 'edit'

        except PatientOrderPhenoList.DoesNotExist:
            c_list = {'checkInput': [], 'textInput': '{}'}
            action = 'add'
        order = Orders.objects.get(id=oid)

    phenolists = PhenoTypeLists.objects.select_related('category').all().order_by('mybackend_phenotypecategory.priority', 'priority', 'name')
    logging(request, 'access')
    return render(request, 'tracker/PatientOrderPhenoType.html', {'phenolists': phenolists, 'c_list':c_list,  'action':action, 'order':order })


@login_required(login_url='/saml/')
def order_phenopypes(request, oid):
    try:
        c_phenolists = OrderPhenoTypes.objects.filter(order_id=oid).order_by('acc')
    except OrderPhenoTypes.DoesNotExist:
        c_phenolists = []
    order = Orders.objects.get(id=oid)
    hpolist=[]
    for plist in c_phenolists:
        hpolist.append(int(plist.acc.split(':')[1]))

    print datetime.now()

    if cache.get('ontology'):
        l = cache.get('ontology')
    else:
        l = LoadOntology.LoadOntology()
        cache.set('ontology', l)

    print l, datetime.now()
    unsortedDiseaseList = l.getSortedDiseaseList(hpolist)
    print unsortedDiseaseList, datetime.now()
    diseaseList = ','.join(unsortedDiseaseList.keys())
    c_diseases = functions.doSQL('Select * from  public_db.external_object_disease where disease_id in (%s)'%diseaseList)

    # sortedDiseaseList = sorted(unsortedDiseaseList.items(), key=lambda x: x[1])  # updated by Young
    newList = []
    for key in unsortedDiseaseList:
        for d in c_diseases:
            if d['disease_id'] == key:
                newList.append({'id': d['db_name']+':'+d['disease_id'], 'title': d['disease_title'], 'score' : unsortedDiseaseList[key]})

    sortedDiseaseList = sorted( newList, key=lambda x:x['score'], reverse=True)  # updated by Young

    logging(request, 'access')
    return render(request, 'tracker/OrderPhenoTypes.html', {'phenolists': c_phenolists, 'order': order, 'sortedlists': sortedDiseaseList})


@login_required(login_url='/saml/')
def add_order_phenopype(request, oid):
    if request.method == 'POST':
        try:
            c_phenolist = OrderPhenoTypes.objects.get(order_id=oid, acc=request.POST['acc'])
            message = 'duplicated'
        except OrderPhenoTypes.DoesNotExist:
            c_phenolist = OrderPhenoTypes(order_id=oid, acc=request.POST['acc'], name=request.POST['name'])
            c_phenolist.save()
            message = 'add new'
        return HttpResponse(message)
    else:
        return HttpResponse('error')


@login_required(login_url='/saml/')
def edit_order_phenopype(request, oid):
    if request.method == 'POST':
        try:
            c_phenolist = OrderPhenoTypes.objects.get(order_id=oid, acc=request.POST['acc'])
            c_phenolist.delete()
            message = 'deleted'
        except OrderPhenoTypes.DoesNotExist:
            message = 'cannot find record'
        return HttpResponse(message)
    else:
        return HttpResponse('error')

@login_required(login_url='/saml/')
def phenotype_hpo(request, acc):
    tid = str(functions.getTermID('acc', acc))
    details = functions.getTermDetails(tid)

    disease = functions.getDiseaseByTermID(tid)
    # genes = functions.getOmimGenes(disease)
    dblist =[]
    for d in disease:
        dblist.append({'dbname': d['db_name'].encode('utf8'), 'id': str(d['disease_id'])})
    logging(request, 'access')
    return render(request, 'tracker/PhenoType.html', {'details':details, 'disease': disease, 'acc':acc, 'dblist': dblist})


@login_required(login_url='/saml/')
def phenotype_graph(request, acc):
    tid = str(functions.getTermID('acc', acc))
    details = functions.getTermDetails(tid)
    relations = functions.getTermRelations(tid)
    logging(request, 'access')
    return render(request, 'tracker/PhenoType_Graph.html', {'details':details, 'relations': json.dumps(relations), 'acc':acc})


@login_required(login_url='/saml/')
def genelists(request):
    c_genelists = GeneLists.objects.select_related('category').order_by('category', 'name')
    newlist = []
    for obj in c_genelists:
        newlist.append({'name':obj.name, 'category':obj.category.name, 'list':obj.list, 'desc':obj.desc, 'id':obj.id})
    logging(request, 'access')
    return render(request, 'tracker/GeneLists.html', {'genelists': json.dumps(newlist)})


@login_required(login_url='/saml/')
def edit_genelist(request):
    if request.method == 'POST':
        form = GeneListsForm(request.POST)
        if request.POST['action'] == 'delete':
            gene = GeneLists.objects.get(id=request.POST['gid'])
            gene.delete()
        elif request.POST['action'] == 'edit':
            gid = request.POST['gid']
            gene = GeneLists.objects.get(id=gid)
            gene.name = request.POST['name']
            gene.list = request.POST['list'].replace('\r\n', ' ')
            gene.desc = request.POST['desc']
            gene.save()
        else:       # add
            form.save()
        return HttpResponseRedirect('/GeneLists/')
    else:
        if not request.META['QUERY_STRING']:
            form = GeneListsForm()
            action = 'add'
            gid=0
        else:
            gid = request.GET.get('gid')
            c_genelist = GeneLists.objects.get(id=gid)
            form = GeneListsForm(instance=c_genelist)
            action = 'edit'
    logging(request, 'access')
    return render(request, 'tracker/EditGeneList.html', {'form': form, 'action':action, 'gid':gid})


@login_required(login_url='/saml/')
def add_patient_order_genelist(request, oid):
    if request.method == 'POST':
        form = OrderGeneListForm(request.POST)
        if request.POST['action'] == 'delete':
            c_genelist = OrderGeneList.objects.get(order_id=request.POST['order'],genelist=request.POST['genelist'])
            c_genelist.delete()
            print 'deleted'
        else:
            print('saved')
            if form.is_valid():
                    form.save()
            else:
                message = form.errors
                messages.error(request, message)
                print ('form error', form.errors.__str__())

        return HttpResponseRedirect('/PatientOrderGeneList/' + oid + '/')
    else:
        form = OrderGeneListForm(initial={'order': oid})
        order = Orders.objects.get(id=oid)
        try:
            genelist = OrderGeneList.objects.select_related('genelist').filter(order_id=oid)
        except OrderGeneList.DoesNotExist:
            print (genelist)
    logging(request, 'access')
    return render(request, 'tracker/PatientOrderGeneList.html', {'genelists': genelist,'form': form, 'order':order })


@login_required(login_url='/saml/')
def edit_patient_order_phenopype(request, pid):
    if request.method == 'POST':
        form = PatientOrderPhenoTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/order/'+str(form.cleaned_data['order'].id) + '/')

    else:
        c_phenotype = PatientOrderPhenoType.objects.get(id=pid)
        form = PatientOrderPhenoTypeForm(instance=c_phenotype)
    logging(request, 'access')
    return render(request, 'tracker/PatientOrderPhenoType.html', {'form': form , 'action': 'edit' })
















#
#
# #################################
# @login_required(login_url='/saml/')
# def phenotypes(request):
#     c_phenotypes = PhenoTypes.objects.all().order_by('name')
#     jsonstring_phenotypes = serializers.serialize('json', c_phenotypes)
#     return render(request, 'tracker/PhenoTypes.html', {'phenotypes': jsonstring_phenotypes})

#
# @login_required(login_url='/saml/')
# def add_phenotype(request):
#     if request.method == 'POST':
#         form = PhenoTypesForm(request.POST, request.FILES)
#         if form.is_valid():
#             print(form, form.cleaned_data, form.cleaned_data['image'])
#             form.save()
#             return HttpResponseRedirect('/Phenotypes/')
#         else:
#             action = 'edit'
#     else:
#         if not request.META['QUERY_STRING']:
#             form = PhenoTypesForm()
#             action = 'add'
#         else:
#             pid = request.GET.get('pid')
#             c_phenotype = PhenoTypes.objects.get(id=pid)
#             form = PhenoTypesForm(instance=c_phenotype)
#             action = 'edit'
#
#     return render(request, 'tracker/PhenoType.html', {'form': form, 'action':action })
