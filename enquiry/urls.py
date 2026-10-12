from django.urls import path
from . import views
urlpatterns = [
    path("enquiry/<int:product_id>/" , views.enquiry_form , name="enquiry_form"),
    path("enquiry_success/" , views.enquiry_success , name="enquiry_success"),

]