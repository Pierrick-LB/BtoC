from django.db import models
from Customer.models import Customer, Payment


class Order(models.Model):
    STATUT_CHOICES = (
        ('pending', 'Pending'),
        ('loading', 'Loading'),
        ('done', 'Done'),
        ('cancel', 'Cancel'),
    )
    
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    products = models.ManyToManyField('Products.Product')
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    shipping_address = models.CharField(max_length=100)
    order_date = models.DateField()
    order_status = models.CharField(max_length=50, choices=STATUT_CHOICES)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


