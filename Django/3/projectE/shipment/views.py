from django.shortcuts import render
from django.http import Http404

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core import serializers
import json
##from rest_framework import serializers


from shipment.models import Item, Job, 거래처, 현장, 출하, 수주, 규격, standard_name, contracts, customers
from shipment.serializers import CustomerSerializer
from django.db import connection

def my_custom_sql(sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    row = cursor.fetchall()
    return row

def index(request):
    shipments = 출하.objects.all()

    standard_names = standard_name.objects.all()
    json_stnames= json.loads(serializers.serialize('json', standard_names))
    request.session['standard_names'] = json_stnames[0]['fields']
    c_customers = customers.objects.all()
    jsonstring_customers = serializers.serialize('json', c_customers)
    return render(request, 'shipment/index.html', {'shipments': shipments, 'customers': jsonstring_customers})

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
    print('logout')
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

def logout(request):
    try:
        del request.session['username']
    except KeyError:
        pass
    return HttpResponse("You're logged out.")