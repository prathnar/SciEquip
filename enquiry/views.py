from django.shortcuts import render , redirect , get_object_or_404
from .models import Enquiry
from .emails import send_enquiry_email
from products.models import Product

def enquiry_form(request , product_id):
    product = get_object_or_404(Product , id= product_id)

    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        message = request.POST.get("message")

        enquiry = Enquiry.objects.create(
            product = product,
            first_name = first_name,
            last_name=last_name,
            phone=phone,
            email=email,
            message=message

        )

      

        send_enquiry_email(enquiry)

        return redirect("enquiry_success")
    
    return render(request , "enquiry/enquiry_form.html" , {"product" : product})

def enquiry_success(request):
    return render(request, "enquiry/enquiry_success.html")