from django.db import models
from django.db.models import CASCADE
from django.contrib.auth.models import User


class Dishes(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='dishes_image/', null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} — {self.price}"


