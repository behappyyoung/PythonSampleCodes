from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.http import (HttpResponse, HttpResponseRedirect,
                         HttpResponseServerError)
from django.core import serializers
from tracker.models import Samples
from .models import Workflows, WorkflowType
from .forms import WorkflowsForm
from mybackend.models import CustomSQL
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import json, yaml
import socket, sys
from logger.models import accessLog, logging
from gims import settings
from httplib import BadStatusLine
import urllib2


if int(sys.version[4:6]) >=9 :  # for python 2.7.9 above..
    newversion = True
    import ssl
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
else:
    newversion = False

if settings.LOCAL:                  # for python 2.7.9 above..
    import ssl
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

from gims.settings import LOOMURL, LOOMURLS


def custom_proc(request):
    return {
        'LOOMURL': settings.LOOMURL,
    }

@login_required(login_url='/saml/')
def index(request):
    if 'username' in request.session:
        print request.session.get('username')
    else:
        return HttpResponseRedirect('/saml/?slo')
    response = urllib2.urlopen(LOOMURL+'data-objects/').read()
    workflows = urllib2.urlopen(LOOMURL+'abstract-workflows/').read()
    fileData = urllib2.urlopen(LOOMURL+'file-data-objects/').read()
    running = urllib2.urlopen(LOOMURL+'run-requests/').read()
    logging(request, 'access')
    return render(request, 'workflows/index.html', {'data':response, 'fileData': fileData, 'workflows':workflows, 'running':running}, context_instance=RequestContext(request, processors=[custom_proc]))

BASE_WORKFLOW_SQL='SELECT w.*, wt.type_name as tname from workflows_workflows w left join workflows_workflowtype wt on w.type_id = wt.id WHERE w.status="A" '


@login_required(login_url='/saml/')
def workflows(request):
    if 'username' in request.session:
        print request.session.get('username')
    else:
        return HttpResponseRedirect('/saml/?slo')

    myc = CustomSQL()
    c_workflows = myc.my_custom_sql(BASE_WORKFLOW_SQL)

    logging(request, 'access')
    return render(request, 'workflows/workflows.html', {'workflows':json.dumps(c_workflows)}, context_instance=RequestContext(request, processors=[custom_proc]))


@login_required(login_url='/saml/')
def workflow_details(request, wid):
    if 'username' in request.session:
        print request.session.get('username')
    else:
        return HttpResponseRedirect('/saml/?slo')

    try:
        if newversion:  # for python 2.7.9 above..
            c_workflow = urllib2.urlopen(LOOMURLS['workflows']+wid+'/', context=ctx).read()
        else:
            c_workflow = urllib2.urlopen(LOOMURLS['workflows']+wid+'/').read()
    except BadStatusLine:
        message = "could not fetch %s" % LOOMURLS['workflows']
        messages.error(request, message)
        return HttpResponseRedirect('/')
    json_workflow = yaml.safe_load(c_workflow)
    logging(request, 'access')
    return render(request, 'workflows/workflow_details.html', {'workflow':json_workflow}, context_instance=RequestContext(request, processors=[custom_proc]))


@login_required(login_url='/saml/')
def define_workflows(request):
    if 'username' in request.session:
        print request.session.get('username')
    else:
        return HttpResponseRedirect('/saml/?slo')
    wf_types = WorkflowType.wf_objects.all()
    type_lists =[]
    for wftype in wf_types:
        type_lists.append({'id':wftype.id, 'type': wftype.type, 'typename': wftype.type_name, 'desc': wftype.desc})
    logging(request, 'access')
    return render(request, 'workflows/workflows_create.html', {'title': 'Create Workflows', 'wf_types': json.dumps(type_lists)},
                  context_instance=RequestContext(request, processors=[custom_proc]))


@login_required(login_url='/saml/')
def edit_workflow(request, wid):
    if request.method == 'POST':
        form = WorkflowsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/workflows/')
    else:
        wf = Workflows.objects.get(id=wid)
        form = WorkflowsForm(instance=wf)
    return render(request, 'workflows/workflow_edit.html', {'form': form, 'wid':wid })

BASE_SAMPLE_SQL='Select * from tracker_samples s left join tracker_sampleorderrel rel on s.id = rel.sample_id ' \
                'join tracker_orders o on o.id = rel.order_id join tracker_relations rt on rel.relation_id = rt.id '

BASE_SAMPLEFILES_SQL='SELECT sf.*, s.asn as asn from tracker_samplefiles sf join tracker_samples s on sf.sample_id = s.id'

LAB_SAMPLE_SQL = 'Select * from tracker_samples s left join tracker_sampleorderrel rel on s.id = rel.sample_id ' \
                  'join tracker_orders o on o.id = rel.order_id join tracker_relations rt on rel.relation_id = rt.id ' \
                  'join tracker_orderstatus os on o.status_id = os.id'

@login_required(login_url='/saml/')
def lab_workflows(request):
    if 'username' in request.session:
        print request.session.get('username')
    else:
        return HttpResponseRedirect('/saml/?slo')
    logging(request, 'access')
    return render(request, 'workflows/lab_workflow.html', {'title': 'Lab Workflows'})


@login_required(login_url='/saml/')
def new_labwork(request):
    if 'username' in request.session:
        print request.session.get('username')
    else:
        return HttpResponseRedirect('/saml/?slo')
    myc = CustomSQL()
    c_samples = myc.my_custom_sql(LAB_SAMPLE_SQL)
    logging(request, 'access')
    return render(request, 'workflows/labwork.html', {'samples':json.dumps(c_samples), 'title': 'New Lab Work'})


@login_required(login_url='/saml/')
def analyses(request):
    if 'username' not in request.session:
        return HttpResponseRedirect('/saml/?slo')

    try:
        if newversion:  # for python 2.7.9 above..
            running = urllib2.urlopen(LOOMURLS['runrequest'], context=ctx).read()
        else:
            running = urllib2.urlopen(LOOMURLS['runrequest']).read()
    except BadStatusLine:
        message = "could not fetch %s" % LOOMURLS['runrequest']
        messages.error(request, message)
        return HttpResponseRedirect('/')
    json_running = yaml.safe_load(running)
    logging(request, 'access')
    return render(request, 'workflows/analyses.html', {'running': json_running}, context_instance=RequestContext(request, processors=[custom_proc]))


@login_required(login_url='/saml/')
def run_analysis(request):
    if 'username' not in request.session:
        return HttpResponseRedirect('/saml/?slo')

    if 'Interpretation' not in request.session.get('role') and 'Manager' not in request.session.get('role'):
        message = " You do not have permission to load  %s" % request.path_info
        messages.error(request, message)
        logging(request, 'UnAuthorized')
        return HttpResponseRedirect('/')

    myc = CustomSQL()
    c_samples = myc.my_custom_sql(BASE_SAMPLE_SQL)
    c_samplefiles = myc.my_custom_sql(BASE_SAMPLEFILES_SQL)
    c_workflows = myc.my_custom_sql(BASE_WORKFLOW_SQL)
    logging(request, 'access')
    return render(request, 'workflows/analysis.html', {'workflows':json.dumps(c_workflows), 'samples':json.dumps(c_samples), 'samplefiles':json.dumps(c_samplefiles)}, context_instance=RequestContext(request, processors=[custom_proc]))


@login_required(login_url='/saml/')
def analysis_details(request, wid):
    if 'username' in request.session:
        print request.session.get('username')
    else:
        return HttpResponseRedirect('/saml/?slo')

    try:
        if newversion:  # for python 2.7.9 above..
            c_analysis = urllib2.urlopen(LOOMURLS['runrequest']+wid+'/', context=ctx).read()
        else:
            c_analysis = urllib2.urlopen(LOOMURLS['runrequest']+wid+'/').read()
    except BadStatusLine:
        message = "could not fetch %s" % LOOMURLS['runrequest']
        messages.error(request, message)
        return HttpResponseRedirect('/')
    json_analysis = yaml.safe_load(c_analysis)
    logging(request, 'access')
    return render(request, 'workflows/analysis_details.html', {'analysis':json_analysis}, context_instance=RequestContext(request, processors=[custom_proc]))


@login_required(login_url='/saml/')
def delete_workflow(request, wid):
    try:
        wf = Workflows.objects.get(id=wid)
        wf.status = '1'
        message = wf.save()
    except:
        message = 'error'

    return HttpResponse(message)
