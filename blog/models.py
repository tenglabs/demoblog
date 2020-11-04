from django.db import models

from django.utils import timezone # timezone import
from django.contrib.auth.models import User # import of User model

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)

    slug = models.SlugField(max_length=250)
    
    content = models.TextField(null=True)

    #new class members

    author = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)

    date_published = models.DateTimeField(default=timezone.now) #date published
    def __str__(self):
        return self.title    

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE) #Foreign Key to Post model

    name = models.CharField(max_length=55)
    
    text = models.TextField()

  
