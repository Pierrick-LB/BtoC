from django.db import models
#from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
#TODO : define comment table here @Hawa , @Maimouna, @Pierrick
#TODO : refactor comment table to use foreign key to user table @Hawa , @Maimouna, @Pierrick
#TODO : define articles tables @Hawa , @Maimouna, @Pierrick

class Comment(models.Model):
    first_name = models.CharField(max_length=100)
    content = models.TextField()
    added = models.DateField()

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return slugify(self.name)
    
class Post(models.Model):
    title = models.CharField(max_length=255)
    #author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, unique=True)
    banner = models.ImageField(upload_to="posts/")
    comments = models.ManyToManyField(Comment, blank=True)
    display = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    def slug(self):
        return slugify(self.title)

    def cat(self):
        return slugify(self.category)

    