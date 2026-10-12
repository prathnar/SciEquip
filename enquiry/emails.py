from django.core.mail import send_mail
from django.conf import settings


def send_enquiry_email(enquiry):
    # ==========================
    # EMAIL TO ADMIN
    # ==========================
    admin_subject = f"New Product Enquiry - {enquiry.product.name}"

    admin_message = f"""
New enquiry received on SciEquip.

Product: {enquiry.product.name}

Customer Details:
Name: {enquiry.first_name} {enquiry.last_name}
Email: {enquiry.email}
Phone: {enquiry.phone}

Message:
{enquiry.message}
"""

    send_mail(
        admin_subject,
        admin_message,
        settings.DEFAULT_FROM_EMAIL,
        [settings.ADMIN_EMAIL],
        fail_silently=False
    )

    # ==========================
    # AUTO-REPLY TO USER
    # ==========================
    user_subject = "We received your enquiry - SciEquip"

    user_message = f"""
Hi {enquiry.first_name},

Thank you for contacting SciEquip regarding
{enquiry.product.name}.

Our team has received your enquiry and will
contact you shortly.

Regards,
LabXplore Team
"""

    send_mail(
        user_subject,
        user_message,
        settings.DEFAULT_FROM_EMAIL,
        [enquiry.email],
        fail_silently=True
    )