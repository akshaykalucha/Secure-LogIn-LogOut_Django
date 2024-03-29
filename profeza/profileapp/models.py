from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
