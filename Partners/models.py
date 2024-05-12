from django.db import models
#todo partenaire hérite de user
class Partenaire(models.Model):
    nom_societe = models.CharField(max_length=100)
    nature_activite = models.CharField(max_length=100)
    adresse = models.CharField(max_length=100)
    email = models.EmailField()
    numero_telephone = models.CharField(max_length=20)
    personne_contact = models.CharField(max_length=100)
    statut_partenariat = models.CharField(max_length=100)
    date_debut_partenariat = models.DateField()
    date_fin_partenariat = models.DateField()
