from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'phone',
        'total_amount',
        'payment_method',
        'created_at',
    )
    list_filter = ('payment_method', 'created_at')
    search_fields = ('first_name', 'phone', 'email')
    inlines = [OrderItemInline]



admin.site.register(OrderItem)