from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def product_list(request):
    return HttpResponse('./productsproduct_list.html')