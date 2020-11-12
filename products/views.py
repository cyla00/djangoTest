from django.shortcuts import render
from django.http import HttpResponse
from .models import * 

# Create your views here.
def productHome(request):
    return render(request, 'products/product_home.html')

def productList(request):
    products = product.objects.all()
    return render(request, 'products/product_list.html', {'products':products})

def productMore(request, P_id):
    single_product = product.objects.filter(id=P_id)
    return render(request, 'products/product_more.html', {'single_product':single_product})


