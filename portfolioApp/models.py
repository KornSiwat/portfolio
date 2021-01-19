import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class ContactMessage(models.Model):
    name = models.CharField(max_length=32, null=False)
    email = models.EmailField(null=False)
    message = models.TextField(max_length=500)
