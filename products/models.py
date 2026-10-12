from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    machine_function = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='product_images/')
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    available = models.BooleanField(default=True)

    def str(self):
        return self.name
