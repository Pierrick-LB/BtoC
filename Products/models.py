from django.db import models



#TODO : define article table here @Hawa , @Maimouna, @Pierrick
#TODO : refactor article table fields @Hawa , @Maimouna, @Pierrick

class Article(models.Model):
    seller= models.ForeignKey('Seller', on_delete=models.CASCADE)  #HERITAGE
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    date = models.DateField()
    category = models.CharField(max_length=50)
    stock = models.IntegerField()
    image = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)