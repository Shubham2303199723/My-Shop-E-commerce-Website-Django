from django.shortcuts import render
from django.views import View
from Store.models import Orders
from Store.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator

class OrderCart(View):
    @method_decorator(auth_middleware)
    def get(self, request):
        customer = request.session.get('customer')
        orders = Orders.get_orders_by_customer(customer)
        print(orders)
        return render (request, 'orders.html', {'orders': orders})