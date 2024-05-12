from django.db import models

class Commentaire(models.Model):
    prenom = models.CharField(max_length=100)
    contenu = models.TextField()
    date = models.DateField()