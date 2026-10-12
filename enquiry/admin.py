from django.contrib import admin
from .models import Enquiry

@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'first_name',
        'phone',
        'email',
        'created_at',
    )
    search_fields = ('first_name', 'phone', 'email', 'product__name')
    list_filter = ('created_at',)
