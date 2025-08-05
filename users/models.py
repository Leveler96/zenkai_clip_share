from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # later i can add fields here like profile_picture, bio, etc
    profile_picture = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(blank=True, null=True)

    # Create your models here.

    def __str__(self):
        return f'{self.user.username}Profile'
