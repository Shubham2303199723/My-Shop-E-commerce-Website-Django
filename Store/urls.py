from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='homepage'),
    path('signup/', signup),
    path ('login/', login),
]
