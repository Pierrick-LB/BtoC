from django.db import models

class Message(models.Model):
    user = models.ForeignKey('Login.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name