from django.db import models

# Create your models here.
class ImgProcessing(models.Model):
    name=models.CharField(max_length=255)
    image=models.ImageField(max_length=255)
