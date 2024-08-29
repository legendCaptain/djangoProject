from django.db import models

# Create your models here.
class django_user_info(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=20)
    age = models.IntegerField()