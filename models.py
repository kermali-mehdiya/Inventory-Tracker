from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class Location(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Inventory(models.Model):
    productname= models.CharField(max_length=100)
    product_code= models.CharField(max_length=3)
    location= models.ForeignKey(Location, on_delete=models.CASCADE)
    quantity = models.IntegerField(validators=[MinValueValidator(1)])
