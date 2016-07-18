from django.shortcuts import render
from django.http import Http404

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core import serializers
import json
##from rest_framework import serializers


from shipment.models import Item, Job, 거래처, 현장, 출하, 수주, 규격, standard_name, contracts, customers, sites
from shipment.serializers import CustomerSerializer
from django.db import connection
from .forms import SitesForm

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def my_custom_sql(sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    ##row = cursor.fetchall()
    row = dictfetchall(cursor)
    print(row)
    return row

def index(request):
    shipments = 출하.objects.all()

    standard_names = standard_name.objects.all()
    json_stnames= json.loads(serializers.serialize('json', standard_names))
    request.session['standard_names'] = json_stnames[0]['fields']
    c_customers = customers.objects.all()
    jsonstring_customers = serializers.serialize('json', c_customers)
    return render(request, 'shipment/index.html', {'shipments': shipments, 'customers': jsonstring_customers})

def edit_customer(request, id):
    try:
        c_customer = customers.objects.get(code=id)
      ##  print(c_customer.id)
        ##c_sites2 = sites.objects.filter(customer_id = c_customer.id)
        c_sites = my_custom_sql("select * from shipment_sites s where customer_id=" + str(c_customer.id))
    except customers.DoesNotExist:
        raise Http404('this customer does not exist')
    print(c_customer.__dict__)
    ##print('c_sites2', c_sites2.__dict__)
    print(c_sites)
    ##jsonstring_customer = serializers.serialize('json', customer)
    return render(request, 'shipment/edit_customer.html', {'customer': c_customer, 'sites' : c_sites})

def edit_site(request, sid):
    try:
        c_sites = sites.objects.get(id=sid)
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = SitesForm(request.POST, instance=c_sites)
            # check whether it's valid:
            if form.is_valid():
                # process the data in form.cleaned_data as required
                ##code = form.cleaned_data['code']
                ##name = form.cleaned_data['name']
                ##address = form.cleaned_data['address']
                ##sites = form.save()
                form.save()
                return HttpResponseRedirect('/recustomers/')

        # if a GET (or any other method) we'll create a blank form
        else:
            form = SitesForm(instance=c_sites)

    except customers.DoesNotExist:
        raise Http404('this customer does not exist')

    return render(request, 'shipment/edit_site.html', { 'form' : form , 'sites':c_sites, 'sid':sid})



def addsite(request, cid):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SitesForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            ##code = form.cleaned_data['code']
            ##name = form.cleaned_data['name']
            ##address = form.cleaned_data['address']
            sites = form.save(commit=False)
            sites.customer = customers.objects.get(id=cid)
            sites.save()
            return HttpResponseRedirect('/recustomers/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SitesForm()

    return render(request, 'shipment/add_site.html', {'form': form, 'cid': cid})

def siteUpdate(request, id):
    sites.objects.filter(id=id).update(name='name')
    return False

def recustomers(request):
    c_customers = customers.objects.all()
    jsonstring_customers = serializers.serialize('json', c_customers)
    return render(request, 'shipment/recustomers.html', {'customers': jsonstring_customers})

def orders(request):
    c_orders2 = my_custom_sql("SELECT c.*, oc.name, sc.name FROM shipment_contracts c join shipment_customers oc on c.order_customer_id =  oc.id join shipment_customers sc on c.sub_customer_id =  sc.id")
    c_orders = contracts.objects.all()
    c_customers = customers.objects.all()
    jsonstring_orders = serializers.serialize('json', c_orders)
    jsonstring_customers =serializers.serialize('json', c_customers)
    return render(request, 'shipment/orders.html', {'orders': jsonstring_orders, 'customers': jsonstring_customers, 'c2' : json.dumps(c_orders2)})


def item_detail(request, id):
    try:
        item = Item.objects.get(id=id)
    except Item.DoesNotExist:
        raise  Http404('this item does not exist')
    return render(request, 'shipment/item_detail.html', {
        'item' : item,
    })

def user_logout(request):
    logout(request) ## user log out
    return render(request, 'shipment/index.html', {})


def user_login(request):
    ##print('hrere', request.user.is_authenticated)
    if request.user.is_active:
        print('user logged in')
        return HttpResponseRedirect('/')

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)
        print('login', username, password, user)
        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                login(request, user)

                request.session['username'] = username
              ##  standard_names = standard_name.objects.all()
              ##  request.session['standard_names'] = serializers.serialize('json', standard_names)
                return HttpResponseRedirect('/')

            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your  account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print("Invalid login details: " + username +","+ password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'shipment/login.html', {})

