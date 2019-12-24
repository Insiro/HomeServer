from django.db import models

# Create your models here.


class tips(models.Model):
    link = models.URLField(null=True, blank=True)
    name = models.CharField(max_length=200)
    writer = models.CharField(max_length=200, null=True)
    memo = models.TextField(max_length=500, null=True, blank=True)
    important = models.BooleanField(default=False)


class notic(models.Model):
    name = models.CharField(max_length=200)
    writer = models.CharField(max_length=200, null=True)
    contents = models.TextField(max_length=4000, null=True)
    important = models.BooleanField(default=False)


class Heros(models.Model):
    SearchKey = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    rarity = models.IntegerField()
    classType = models.CharField(max_length=20)
    element = models.CharField(max_length=10)
