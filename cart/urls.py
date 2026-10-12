from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('', views.view_cart, name='view_cart'),
    path("remove/<int:product_id>/" , views.remove_cart , name="remove_cart"),
    path("decrease/<int:product_id>/", views.decrease_cart , name="decrease_cart"),
    path('checkout/', views.checkout, name='checkout'),
    path('checkout_success/', views.checkout_success, name='checkout_success')
]