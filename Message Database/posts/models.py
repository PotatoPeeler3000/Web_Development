from django.db import models

# Create your models here.

#Originally added this so we could see our posts from our homepage
class Post (models.Model):
    text = models.TextField()

#Then added this so the post would display the first 50 characters in it
    def __str__(self):
        return self.text[:50]