from django.shortcuts import render, redirect
from Store.models.product import product
from Store.models.category import category
from django.views import View
from django.http import HttpResponse


class Index(View):
    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
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
    
    def post (self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity-1
                else:
                    cart[product] = quantity+1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        print('cart',request.session['cart'])
        return redirect('homepage')
        