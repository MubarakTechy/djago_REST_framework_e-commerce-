from django.db import models
from django.db import models
from categories.models import Category

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1) 
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name