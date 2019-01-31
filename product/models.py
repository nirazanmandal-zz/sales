from django.db import models
from category.models import Category


# Create your models here.
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    pname = models.CharField(max_length=120)
    quantity = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    total = models.CharField(max_length=120)
    description = models.TextField(max_length=150, null=True, blank=True)
    is_deleted = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    class Meta:
        db_table = 'product'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.pname
