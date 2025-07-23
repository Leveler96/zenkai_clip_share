from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # later i can add fields here like profile_picture, bio, etc

# Create your models here.

    def __str__(self):
        return f'{self.user.username}Profile'
