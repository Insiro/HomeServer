from django.db import models

# Create your models here.
class tips(models.Model):
    link = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    writer = models.CharField(max_length=200, null=True)
    memo = models.CharField(max_length=200, null=True)
    important = models.BooleanField(default=False)
class notic(models.Model):
    name = models.CharField(max_length=200)
    writer = models.CharField(max_length=200, null=True)
    contents = models.CharField(max_length=4000, null=True)
