from django.db import models

# Create your models here.
class UserInfo(models.Model):
    user=models.CharField(max_length=32)
    pwd=models.CharField(max_length=32)
    sex=models.CharField(max_length=8)
    feature=models.CharField(max_length=64)