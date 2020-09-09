from django.db import models

# Create your models here.

#NEW
class Post (models.Model):
    text = models.TextField()
#NEW EDIT
    def __str__(self):
        return self.text[:50]