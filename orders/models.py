from django.db import models
from products.models import Product

# Create your models here.
class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=10)
    payment_method = models.CharField(max_length=50 , default="cash on delivery")
    total_amount = models.DecimalField(max_digits=10 , decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)


    
    def __str__(self):
        return f"Order #{self.id} - {self.first_name}"    
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order , on_delete=models.CASCADE , related_name="items")
    product = models.ForeignKey(Product , on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10 , decimal_places=2)


    def __str__(self):
        return f"{self.product.name} (order id #{self.order.id})"