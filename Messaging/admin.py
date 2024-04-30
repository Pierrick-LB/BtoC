from django.contrib import admin
from .models import Message

#Enregistrer Message dans admin pour que ça soit visible
admin.site.register(Message)