from django.db import models
from django.utils import timezone

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Expense(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, default=None)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    datetime = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=100, choices=(("Received", "Received"), ("Spent", "Spent")), default="Spent")
    amount = models.FloatField(default=0.0)
    description = models.CharField(max_length=100, blank=True, null=True, default=None)

    class Meta:
        ordering = ["-datetime"]

    def __str__(self):
        return f"{self.user} {self.datetime} {self.amount}"
