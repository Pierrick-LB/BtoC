from django.db import models

class Message(models.Model):
    nom_complet = models.CharField(max_length=255)
    sujet = models.CharField(max_length=100)
    contenu = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sujet} - {self.nom_complet}"