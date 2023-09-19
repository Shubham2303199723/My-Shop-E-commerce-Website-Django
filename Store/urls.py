from django.contrib import admin
from django.urls import path
from .views import home, login, signup, cart
from .views.login import Logout
from .views.checkout import CheckOut


urlpatterns = [
    path('', home.Index.as_view(), name='homepage'),
    path('signup/', signup.Signup.as_view(), name='signup'),
    path ('login/', login.Login.as_view(), name='login'),
    path('logout/', Logout, name='logout'),
    path('cart/', cart.Cart.as_view(), name='cart'),
    path('checkout', CheckOut.as_view(), name='checkout'),
]
