from django.shortcuts import redirect
from django.views import View
from Store.models.product import product


class CheckOut(View):
    def post(self, request):

        
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = product.get_products_by_id(list(cart.keys()))
        print(address, phone, customer, cart ,products)
        return redirect ('cart')