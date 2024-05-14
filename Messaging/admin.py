from django.contrib import admin
from .models import Message



@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'added')
    search_fields = ('name', 'subject')
    list_filter = ('added',) 

