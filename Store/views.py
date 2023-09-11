from django.http import HttpResponse
from django.shortcuts import render
from .models.product import product

# Create your views here.

def index(request):
    prds = product.get_all_products()
    return render(request, "index.html", {'products' : prds})    