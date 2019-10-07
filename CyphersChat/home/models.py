from django.db import models

# Create your models here.
class projects(models.Model):
    name =models.CharField(max_length=200)     
    kate = models.IntegerField()
    context=models.CharField(max_length=200,null=True,blank=True)
    icon = models.URLField(max_length=1000,null=True,blank=True)
    date= models.DateField(null=True,blank=True)
class project_Img(models.Model):
    projects_id = models.IntegerField()
    img = models.URLField(max_length=1000)
class Kategorie(models.Model):
    name = models.CharField(max_length=20)
class show_pro(models.Model):
    project_id = models.IntegerField()