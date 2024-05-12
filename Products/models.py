from django.db import models



#TODO : define article table here @Hawa , @Maimouna, @Pierrick
#TODO : refactor article table fields @Hawa , @Maimouna, @Pierrick

class Article(models.Model):
    numero_article = models.IntegerField()
    nom = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    date = models.DateField()
    categorie = models.CharField(max_length=50)
    stock = models.IntegerField()
    image = models.URLField()
