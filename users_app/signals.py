from django.dispatch import receiver
from django.db.models.signals import post_delete, post_save


from django.contrib.auth.models import User
from users_app.models import Profile


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
