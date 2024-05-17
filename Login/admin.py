from django.contrib import admin
from .models import User    



@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    display = ('id', 'name', 'email', 'is_staff', 'is_active', 'phone')
    search_fields = ('username', 'email')
