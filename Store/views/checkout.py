from django.shortcuts import redirect
from django.views import View
from Store.models.product import product
from Store.models.orders import Orders
from Store.models.customer import Customer


class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = product.get_products_by_id(list(cart.keys()))
        print(products)
        print(address, phone, customer, cart, products)
        for prodt in products:
            print(cart.get(str(prodt.id)))
            order = Orders(customer=Customer(id=customer),
                           product=prodt,
                           price=prodt.price,
                           address=address,
                           phone=phone,
                           quantity=cart.get(str(prodt.id)))
            order.save()
        request.session['cart'] = {}
        return redirect('cart')
