from django.shortcuts import render
from django.http import Http404

##from django.http import HttpResponse

from shipment.models import Item

def index(request):
    items = Item.objects.exclude(amount=0)
    return render(request, 'shipment/index.html', {
        'items': items,
    })
def item_detail(request, id):
    try:
        item = Item.objects.get(id=id)
    except Item.DoesNotExist:
        raise  Http404('this item does not exist')
    return render(request, 'shipment/item_detail.html', {
        'item' : item,
    })