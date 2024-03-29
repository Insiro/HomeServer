from django.db import models

# Create your models here.
class Kategorie(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name
class projects(models.Model):
    name =models.CharField(max_length=200)     
    kate = models.ForeignKey(Kategorie, on_delete = models.SET_NULL, null=True)
    context=models.TextField(null=True, blank = True)
    icon = models.ImageField(upload_to="icon",null=True,blank=True)
    date= models.DateField(null=True,blank=True)
    def __str__(self):
        return self.name

class project_Img(models.Model):
    projects_id = models.ForeignKey(projects,on_delete = models.CASCADE)
    img = models.ImageField(upload_to="home/image")
    #img = models.URLField(max_length=1000)
    
class show_pro(models.Model):
    project_id = models.IntegerField()

class careers(models.Model):
    projectName = models.CharField(max_length = 50)
    role = models.CharField(max_length = 100)
    duration = models.CharField(max_length = 100)
    def __str__(self):
        return self.projectName

class myInfo(models.Model):
    introduce = models.TextField(null = True, blank = True)

class skill(models.Model):
    skillName = models.CharField(max_length = 50)
    studying = models.BooleanField(default=False)
    def __str__(self):
        return self.skillName

class usableLanguages(models.Model):
    lang = models.CharField(max_length = 50)
    def __str__(self):
        return self.lang

class history(models.Model):
    name = models.CharField(max_length = 100)
    period = models.CharField(max_length = 100)
    def __str__(self):
        return self.name