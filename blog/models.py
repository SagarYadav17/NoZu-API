from django.db import models
from django.utils.text import slugify

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField(max_length=500)
    content = models.TextField()
    published_date = models.DateField(blank=True, null=True)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super(Post, self).save(*args, **kwargs)
