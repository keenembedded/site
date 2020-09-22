from django.contrib import admin
from django.urls import path

from .views import index , product, about,contact

urlpatterns = [
    path("",index,name="index"),
    path("product/",product,name="product"),
    path("about/",about,name="product"),
    path('contact/', contact , name='contact'),
]