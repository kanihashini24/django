from django.db import models

# Create your models here.

# Create your models here.
class student(models.Model):
    Name=models.CharField(max_length=20,default="")
    Age=models.IntegerField(default="")
    Contact=models.IntegerField(default="")
    Address=models.CharField(max_length=50,default="")
    Mail=models.CharField(max_length=50,default="")
    

class Datas(models.Model):
    Name=models.CharField(max_length=20,default="")
    Age=models.IntegerField(default="")
    Address=models.CharField(max_length=50,default="")
    Mail=models.CharField(max_length=50,default="")



