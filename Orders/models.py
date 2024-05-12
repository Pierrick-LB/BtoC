from django.db import models

class Order(models.Model):
    STATUT_CHOICES = (
        ('pending', 'Pending'),
        ('loading', 'Loading'),
        ('done', 'Done'),
        ('cancel', 'Cancel'),
    )
    articles_commandes = models.TextField()
    adresse_livraison = models.CharField(max_length=100)
    date_commande = models.DateField()
    statut_commande = models.CharField(max_length=50, choices=STATUT_CHOICES)
    methode_paiement = models.CharField(max_length=50)
    montant_total = models.DecimalField(max_digits=10, decimal_places=2)
