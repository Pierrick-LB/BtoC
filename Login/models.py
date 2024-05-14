from django.db import models

#TODO : define user table here @Hawa , @Maimouna, @Pierrick
#TODO : refactor django user table to use authentification by phone number @Fallou


class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return self.email
