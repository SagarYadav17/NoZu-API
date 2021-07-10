from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250, blank=True, null=True)
    image = models.ImageField(
        upload_to='media/uploads/post', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.user
