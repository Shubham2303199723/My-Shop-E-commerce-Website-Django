from django.shortcuts import render, redirect
from Store.models.product import product
from Store.models.category import category
from django.views import View


class Index(View):
    def get(self, request):
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
        print(request.session.get('email'))
        print(request.session.get('customer_id'))
        return render(request, "index.html", data)
    def post (self, request):
        product = request.POST.get('product')
        print(product)
        return redirect('homepage')
        