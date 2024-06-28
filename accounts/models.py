from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  bio = models.TextField(max_length=500, blank=True)
  nation = models.CharField(max_length=30, blank=True)
  birth_date = models.DateField(null=True, blank=True)
  schooll = models.CharField(max_length=100, blank=True)
  major = models.CharField(max_length=30, blank=True)

  def __str__(self):
    return self.user.username