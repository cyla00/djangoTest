from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def product_list(request):
    return render(request, 'products/product_list.html')