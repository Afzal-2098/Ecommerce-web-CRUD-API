from django.db import models

# Model for product
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='product_images/')
    date = models.DateField()
