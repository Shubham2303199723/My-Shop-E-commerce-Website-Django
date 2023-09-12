from django.http import HttpResponse
from django.shortcuts import render
from .models.product import product
from .models.category import category

# Create your views here.

def index(request):
    products = None
    categories = category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = product.get_all_products_by_categoryid(categoryID)
    else:
        products = product.get_all_products()
    data = {}
    data ['products'] = products
    data ['categories'] = categories
    return render(request, "index.html", data) 


def signup(request):
    if (request.method == 'GET'):
        return render(request,'signup.html')
    else:
        return HttpResponse('Recived Post Request')
