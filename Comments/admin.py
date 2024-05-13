from django.contrib import admin
from .models import *
# Register your models here.
#TODO : Register alls table here in order to display them on the panel admin @Hawa , @Maimouna, @Pierrick

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'content', 'added')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','category','created', 'updated')