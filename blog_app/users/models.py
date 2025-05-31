from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(max_length=500)

    def __str__(self):
        # Returns the username with "Profile" suffix for easy identification
        return f'{self.user.username} Profile'
    
    def save(self, *args, **kwargs):
        # Pass on any args/kwargs to the parent save method
        super().save(*args, **kwargs)

        # Resize image if larger than 300x300
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
