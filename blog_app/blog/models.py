from django.db import models
from django.contrib.auth.models  import User 
from django.utils import timezone
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk}) # reverse  will return the path as a string to the view, and kwargs is a dictionary of keyword arguments that will be passed to the URL pattern.
    



# Create your models here.# how the data are stored in the database
# and how they are related to each other. The Post model represents a blog post with fields for title, content, date posted, and author.
