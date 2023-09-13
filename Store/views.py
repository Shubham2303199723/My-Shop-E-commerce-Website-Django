from django.http import HttpResponse
from django.shortcuts import render ,redirect
from django.contrib.auth.hashers  import make_password,check_password
from .models.product import product
from .models.category import category
from .models.customer import Customer



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

def validateCustomer(customer):
    error_message = None
    if (not customer.first_name):
        error_message = "First Name Required.."
    elif len(customer.first_name) < 4:
        error_message = "First Name Char should be long more then 4 Char"
    elif(not customer.last_name):
        error_message = "last Name Required"
    elif len(customer.last_name) < 4:
        error_message = "Last Name Char should be long more then 4 Char"
    elif(not customer.email):
        error_message = "Email Must Required"
    elif len(customer.email) < 5:
        error_message = "Email Char should be long more then 4 Char"
    elif(not customer.password):
        error_message = "Password Required"
    elif len(customer.password) < 6:
        error_message = "Password Char should be long more then 6 Char"    
    elif(not customer.phone):
        error_message = "Phone number Required"
    elif customer.isExists():
        error_message = 'Email Address is Already Registered..'
    return error_message

def registerUser(request):
    postdata = request.POST
    email = postdata.get('email')
    password = postdata.get('password')
    first_name = postdata.get('firstname')
    last_name = postdata.get('lastname')
    phone = postdata.get('phone')
    value = {
        'first_name' : first_name,
        'last_name' : last_name,
        'phone' : phone,
        'email' : email,            
        }
    error_message = None
    customer = Customer (first_name = first_name,
                            last_name = last_name,
                            email = email,
                            password = password,
                            phone = phone,
                            )
    error_message = validateCustomer(customer)
    
    

    if not error_message:
        customer.password = make_password(customer.password)
        customer.register()
        return redirect('homepage')
    else:
        data = {
            'error' : error_message,
            'values' : value
        }
        return render(request,'signup.html', data)

def signup(request):
    if (request.method == 'GET'):
        return render(request,'signup.html')
    else:
        return registerUser(request)

def login(request):
    if (request.method == 'GET'):
        return render (request, 'login.html')
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                return redirect('homepage')
            else:
                error_message = 'Email or password Invalid!!'
        else:
            error_message = 'Email & password Are Invalid!!'
        return (request , 'login.html', {'error': error_message})
    
        
