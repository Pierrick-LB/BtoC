from django.db import models

class Message(models.Model):
    full_name = models.CharField(max_length=255)
    subject = models.CharField(max_length=100)
    content = models.TextField()
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sujet} - {self.nom_complet}"