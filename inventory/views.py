from django.shortcuts import render
from django.http import Http404

from inventory.models import Item

def index(request):
    items = Item.objects.exclude(amount=0)
    return render(request, 'inventory/index.html', {
        'items': items,

    })

def item_detail(request, id):
    try:
        item = Item.objects.get(id=id)
    except Item.DoesNotExist:
        raise Http404('This item does not exist')
    return render(request, 'inventory/item_detail.html', {
        'item': item,
    })

def out_of_stock(request):
    items = Item.objects.exclude(amount=10)
    return render(request, 'inventory/out_of_stock.html', {
        'items': items,
    })
