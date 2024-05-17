from django.contrib import admin
from .models import Customer, Payment


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    display = ('id', 'user', 'created_at')


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'payment_method', 'amount', 'created_at')
