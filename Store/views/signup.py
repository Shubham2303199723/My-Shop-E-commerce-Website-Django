from django.shortcuts import render ,redirect
from django.contrib.auth.hashers  import make_password
from Store.models.customer import Customer
from django.views import View


class Signup(View):
    def get(self, request):
        return render(request,'signup.html')
    def post(self, request):
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
        error_message = self.validateCustomer(customer)
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
    def validateCustomer(self, customer):
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