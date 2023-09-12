from django.http import HttpResponse
from django.shortcuts import render
from .models.product import product
from .models.category import category
from .models.customer import Customer

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
        postdata = request.POST
        email = postdata.get('email')
        password = postdata.get('password')
        first_name = postdata.get('firstname')
        last_name = postdata.get('lastname')
        phone = postdata.get('phone')

        error_message = None

        if (not first_name):
            error_message = "First Name Required.."
        elif len(first_name) < 4:
            error_message = "First Name Char should be long more then 4 Char"
        elif(not last_name):
            error_message = "last Name Required"
        elif len(last_name) < 4:
            error_message = "Last Name Char should be long more then 4 Char"
        elif(not email):
            error_message = "Email Must Required"
        elif len(email) < 5:
            error_message = "Email Char should be long more then 4 Char"
        elif(not password):
            error_message = "Password Required"
        elif len(password) < 6:
            error_message = "Password Char should be long more then 4 Char"    
        elif(not phone):
            error_message = "Phone number Required"
          
        if not error_message:
            customer = Customer (first_name = first_name,
                                last_name = last_name,
                                email = email,
                                password = password,
                                phone = phone,
                                )
            customer.register()
        else:
            return render(request, 'signup.html', {'error' : error_message})
