from django.contrib import admin

#New import that I added
from .models import Post

# Register your models here.

admin.site.register(Post)