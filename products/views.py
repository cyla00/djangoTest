from django.shortcuts import render
from django.http import HttpResponse
from .models import * 

# Create your views here.
def product_list(request):
    products = product.objects.all()
    return render(request, 'products/product_list.html', {'products':products})