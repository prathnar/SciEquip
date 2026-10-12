from django.db import models
from products.models import Product

class Enquiry(models.Model):
    product = models.ForeignKey(Product , on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def _str_(self):
        return f"Enquiry for {self.product.name} by {self.first_name}"
