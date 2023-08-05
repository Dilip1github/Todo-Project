from django.db import models

# Create your models here.

class course(models.Model):
    cname = models.CharField(max_length=50)
    cdur = models.CharField(max_length=20)
    cprice = models.CharField(max_length=20)

class student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
