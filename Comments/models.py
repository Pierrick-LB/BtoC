from django.db import models


#TODO : define comment table here @Hawa , @Maimouna, @Pierrick
#TODO : refactor comment table to use foreign key to user table @Hawa , @Maimouna, @Pierrick
#TODO : define articles tables @Hawa , @Maimouna, @Pierrick

class Commentaire(models.Model):
    prenom = models.CharField(max_length=100)
    contenu = models.TextField()
    date = models.DateField()