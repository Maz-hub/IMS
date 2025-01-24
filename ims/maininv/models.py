from django.db import models

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=255)  # Name of the product
    origin_country = models.CharField(max_length=100)  # Country of origin
    color = models.CharField(max_length=50, blank=True, null=True)  # Optional color
    material = models.CharField(max_length=100, blank=True, null=True)  # Optional material
    approx_weight = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Weight in kg
    cost_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Cost price of the product
    description = models.TextField(blank=True, null=True)  # Optional description of the product
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the product was created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when the product was last updated

    def __str__(self):
        return self.product_name
