 #Signals are a way for Django apps to "listen" to certain events and automatically run code when that event happens.
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender= User)#It listens for the post_save signal (after a User is saved). #If a new User is created (created == True), then:It creates a new Profile object automatically linked to that user
def create_profile(sender, instance, created, **kwargs):  
    if created:
        Profile.objects.create(user=instance) #instance is the User object itself.

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


#sender=user only tells Django that the signal comes from the User model. It doesn't give you access to the actual User object that was created.