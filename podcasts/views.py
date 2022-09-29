from pyexpat.errors import messages
from django.shortcuts import render
from .models import Item


def render_items (request):
    
    items = Item.objects.all()
    context =  {'items' : items}
    return render (request, 'items.html', context)

