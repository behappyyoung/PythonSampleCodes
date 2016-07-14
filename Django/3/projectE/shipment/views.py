from django.shortcuts import render
from django.http import Http404

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core import serializers
import json
##from rest_framework import serializers


from shipment.models import Item, Job, 거래처, 현장, 출하, 수주
from shipment.serializers import CustomerSerializer

def index(request):
    shipments = 출하.objects.all()
    customers = 거래처.objects.all()
    json_customers = serializers.serialize('json', customers)
    print(customers)
##    serializer = CustomerSerializer(customers)
##    print(serializer.data)
    customers_list = list(customers)
    print(customers_list)
    for c in customers:
        print(c.거래처명)
    print(json_customers)
    print(json.dumps(json_customers, ensure_ascii=False).encode("utf8"))
    return render(request, 'shipment/index.html', {'shipments': shipments, 'customers': json_customers})

def orders(request):
    orders = 수주.objects.all()
    json_orders = serializers.serialize('json', orders)
    print(orders)
    return render(request, 'shipment/orders.html', {'orders': json_orders})


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
    print('hrere', request.user.is_authenticated)
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