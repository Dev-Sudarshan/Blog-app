from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpg',upload_to='profile_pics')
    bio=models.TextField(max_length='500')

    def __str__(self):   ## __str__ method is used to return a string representation of the object.
        ## In this case, it returns the username of the user associated with the profile.it determines how each object is displayed in the admin interface and other places.
        return f'{self.user.username}Profile'
    
    def save(self):
        super().save()

        img= Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
    

    
# Create your models here.
