from django.db import models

# Create your models here.
class FilePost(models.Model):
    username = models.CharField(max_length=30)
    text = models.TextField()
    expiry = models.CharField(max_length=5)
    filename = models.CharField(max_length=150)
