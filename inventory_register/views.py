from django.shortcuts import render,redirect
from .forms import ProductForm
from django.http import HttpResponse
from .models import Inventory
import csv

# Create your views here.

def product_list(request):
    context = {'product_list':Inventory.objects.all()}
    return render(request, "inventory_register/product_list.html",context)

def product_form(request, id=0):
    if request.method == "GET":
        if id==0:
            form=ProductForm()
        else:
            inventory = Inventory.objects.get(pk=id)
            form = ProductForm(instance=inventory)
        return render(request,"inventory_register/product_form.html",{'form':form})
   
    else:
        if id == 0:
            form = ProductForm(request.POST)
        else:
            inventory = Inventory.objects.get(pk=id)
            form = ProductForm(request.POST,instance=inventory)
        if form.is_valid():
            form.save()
        return redirect('/inventory/list')
   
    form = ProductForm()
    return render(request, "inventory_register/product_form.html", {'form':form})

def product_delete(request,id):
    inventory = Inventory.objects.get(pk=id)
    inventory.delete()
    return redirect('/inventory/list')

def export(request):
    response = HttpResponse(content_type='text/csv')
    
    writer = csv.writer(response)
    writer.writerow(['Product Name','Product Code','Quantity'])

    for inventory in Inventory.objects.all().values_list('productname','product_code','quantity'):
        writer.writerow(inventory)

    response['Content-Disposition']='attachment; filename="inventory.csv"'
    return response