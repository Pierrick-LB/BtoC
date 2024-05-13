from django.db import models

# Create your models here.

#TODO : define seller table ===> user table ( foreign key ) @Hawa , @Maimouna, @Pierrick
class Seller(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey('Login.User', on_delete=models.CASCADE)  #HERITAGE
    activity = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    contacts = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
