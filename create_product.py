import os
import django
from datetime import datetime


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'B2C.settings')  
django.setup()
from Products.models import Product

product = Product.objects.get(id=11) 
product.delete()






# product = Product(name="Apple", price=2, description ="an apple", category="fruit", stock=2, image="fruite-item-1.jpg",
# created_at=datetime.now(), updated_at=datetime.now(),seller_id=1) 

# product.save()



# # Récupérer tous les produits
# all_products = Product.objects.all()
# print(all_products)
