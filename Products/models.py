from django.db import models


class Article(models.Model):
    numero_article = models.IntegerField()
    nom = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    date = models.DateField()
    categorie = models.CharField(max_length=50)
    stock = models.IntegerField()
    image = models.URLField()