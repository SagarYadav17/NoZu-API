"""
User identity related models
"""

from django.db import models
from django.dispatch import receiver

from django.contrib.auth.models import User
from django.db.models.signals import post_delete, post_save


# Create your models here.

class Profile(models.Model):
    """
    Profile Model for User
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    full_name = models.CharField(max_length=50, blank=True, null=True)
    profile_image = models.ImageField(
        upload_to='media/uploads/profile_image', blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return str(self.user)


# Signals


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    Signal for creating profile when new user register
    """

    if created:
        Profile.objects.create(user=instance)
        print('Profile created!')


@receiver(post_delete, sender=Profile)
def delete_user(sender, instance, **kwargs):
    """
    Signal for deleting User when user delete profile
    """

    User.objects.get(id=instance.user.id).delete()
    print('User is deleted')
