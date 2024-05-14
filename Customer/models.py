from django.db import models

class Customer(models.Model):
    user = models.ForeignKey('Login.User', on_delete=models.CASCADE)  #HERITAGE
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




#TODO : ADD payment table and link it to customer table
