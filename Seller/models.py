from django.db import models


class Seller(models.Model):
    user = models.ForeignKey('Login.User', on_delete=models.CASCADE)  #HERITAGE
    activity = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
