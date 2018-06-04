from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from pdb_app.models import Item, Category


def index(request):
    template = loader.get_template('index.html')
    context = {
        'categories': Category.objects.all()
    }
    return HttpResponse(template.render(context, request))

def item(request,item_id):
    try:
        itm = Item.objects.get(id=item_id)
    except Item.DoesNotExist:
        itm = None
    template = loader.get_template('item.html')
    context = {
        'item': itm
    }
    return HttpResponse(template.render(context, request))