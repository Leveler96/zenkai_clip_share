from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Clip(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_uploaded = models.DateField(auto_now_add=True)
    video_file = models.FileField(upload_to='clips/raw_uploads')

    converted_video_file = models.FileField(upload_to='clips/converted', null=True, blank=True)

    uploader = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
