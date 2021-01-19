import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)


class ContactMessage(models.Model):
    name = models.CharField(max_length=32, null=False)
    email = models.EmailField(null=False)
    message = models.TextField(max_length=500)


class Achievement(models.Model):
    name = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=255, null=False)
    year = models.PositiveIntegerField(
        default=current_year(), validators=[MinValueValidator(2000), max_value_current_year])
