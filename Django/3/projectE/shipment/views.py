from django.shortcuts import render
from django.http import Http404

##from django.http import HttpResponse

from shipment.models import Item

def index(request):
    items = Item.objects.exclude(amount=0)
    return render(request, 'shipment/index.html', {
        'items': items,
    })