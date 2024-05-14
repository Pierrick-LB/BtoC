from django.db import models
from django.contrib.auth.models import User


class Partner(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey('Login.User', on_delete=models.CASCADE)
    activity = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    contacts = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    started_date = models.DateField()
    ended_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
