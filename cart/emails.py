from django.core.mail import send_mail
from django.conf import settings

def send_order_emails(order):

    #email to customer

    subject = "Order Confirmed -= SciEquip"
    message = f"""
Hi {order.first_name},

Thank you for your order at SciEquip.

Order ID: {order.id}
Total Amount: ₹{order.total_amount}
Payment Method: {order.payment_method}

We will contact you shortly.

Regards,
SciEquip Team
"""
    


    send_mail(
        subject ,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [order.email],
        fail_silently = False
    )


    #email to admin (me)

    admin_subject = f"New Order Received - Order #{order.id}"
    admin_message = f"""
New order placed.

Customer: {order.first_name} {order.last_name}
Phone: {order.phone}
Email: {order.email}
Total: ₹{order.total_amount}
"""

    send_mail(
        admin_subject,
        admin_message,
        settings.DEFAULT_FROM_EMAIL,
        [settings.ADMIN_EMAIL],
        fail_silently=False
    )