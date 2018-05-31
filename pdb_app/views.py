from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from pdb_app.models import Item


def index(request):
    template = loader.get_template('index.html')
    context = {
        'items': Item.objects.all()
    }
    return HttpResponse(template.render(context, request))

def item(request,item_id):
    template = loader.get_template('item.html')
    context = {
        'item': Item.objects.get(id=item_id)
    }
    return HttpResponse(template.render(context, request))