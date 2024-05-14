from django.db import models
from django.contrib.auth.models import User


class Order(models.Model):
    STATUT_CHOICES = (
        ('pending', 'Pending'),
        ('loading', 'Loading'),
        ('done', 'Done'),
        ('cancel', 'Cancel'),
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    products = models.ManyToManyField('Products.Product')
    shipping_address = models.CharField(max_length=100)
    order_date = models.DateField()
    order_status = models.CharField(max_length=50, choices=STATUT_CHOICES)
    payment_method = models.CharField(max_length=50)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

