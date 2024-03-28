from django.shortcuts import render
from django.views import View
from Store.models import Orders

class OrderCart(View):
    def get(self, request):
        customer = request.session.get('customer')
        orders = Orders.get_orders_by_customer(customer)
        print(orders)
        return render (request, 'orders.html', {'orders': orders})