from django.urls import path
from . import views

urlpatterns =[
    path("" , views.home , name="home"),
    path("contact/" , views.contact , name="contact"),
    path("about/" , views.about , name="about"),
    path("products/" , views.product_list , name="product_list"),
    path("product_detail/<int:id>/" , views.product_detail , name="product_detail"),
]