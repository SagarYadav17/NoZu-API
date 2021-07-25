from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

# Create your models here.


class Profile(models.Model):
    """
    Profile Model for User
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    full_name = models.CharField(max_length=50, blank=True, null=True)
    profile_image = models.ImageField(
        upload_to='media/uploads/profile_image', blank=True, null=True)
    country = CountryField(countries_flag_url='//flags.example.com/{code}.png')

    def __str__(self):
        return str(self.user)
