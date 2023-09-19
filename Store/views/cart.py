from django.shortcuts import render
from Store.models.product import product
from django.views import View


class Cart(View):
    def get(self, request):
        ids = list(request.session.get('cart').keys())
        products = product.get_products_by_id(ids)
        print(products)
        return render(request, 'cart.html', {'products': products})