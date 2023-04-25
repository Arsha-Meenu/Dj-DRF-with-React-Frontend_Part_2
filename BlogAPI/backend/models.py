from django.db import models
from django.contrib.auth.models import  User


class Articles(models.Model):
    title = models.CharField(max_length= 255)
    description = models.TextField()
    slug  = models.SlugField(max_length=200,unique=True)
    published = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='articles')

    def __str__(self):
        return self.slug