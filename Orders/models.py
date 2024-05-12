from django.db import models



#TODO : define order table ===> user table ( foreign key ) @Hawa , @Maimouna, @Pierrick
#TODO : define order table ===> articles table ( foreign key ) @Hawa , @Maimouna, @Pierrick
#TODO : define order table ===> payment table ( foreign key ) @Hawa , @Maimouna, @Pierrick
#TODO : refactor tables fields @Hawa , @Maimouna, @Pierrick

class Order(models.Model):
    STATUT_CHOICES = (
        ('pending', 'Pending'),
        ('loading', 'Loading'),
        ('done', 'Done'),
        ('cancel', 'Cancel'),
    )
    products = models.ManyToManyField('Products.Product')
    adresse_livraison = models.CharField(max_length=100)
    date_commande = models.DateField()
    statut_commande = models.CharField(max_length=50, choices=STATUT_CHOICES)
    methode_paiement = models.CharField(max_length=50)
    montant_total = models.DecimalField(max_digits=10, decimal_places=2)
