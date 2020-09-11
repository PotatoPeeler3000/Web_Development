from django.db import models

# Create your models here.
#This is all new information to the file

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )

    body = models.TextField()

    def __str__(self):
        return self.title
