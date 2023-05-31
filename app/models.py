from django.db import models

# Create your models here.
class Topic(models.Model):
    Tname=models.CharField(max_length=100)
    Subname=models.CharField(max_length=100)

   