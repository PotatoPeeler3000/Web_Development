from django.contrib import admin
from .models import Post #We add this so we can use our Post class we made from our models file

# Register your models here.
#This says that when we visit the admin site we will register this Post class
admin.site.register(Post)