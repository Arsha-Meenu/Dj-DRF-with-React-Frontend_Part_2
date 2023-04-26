from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    title = models.CharField(max_length= 255)
    body = models.TextField()
    slug = models.SlugField(max_length=255,unique=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='questions')
    published = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title


class Answer(models.Model):
    published = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    question = models.ForeignKey(Question,on_delete=models.CASCADE,related_name='answers')
    author = models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.question.title