from django.db import models

class Users(models.Model):
    nombre= models.CharField(max_length=15)
    apellido= models.CharField(max_length=15)
    email= models.EmailField(max_length=100,unique=True)
    password=models.CharField(max_length=15)

   

class Products(models.Model):
    title= models.CharField(max_length=15)
    description= models.CharField(max_length=100)
    price= models.IntegerField()
    stock=models.IntegerField()
    imagen= models.ImageField(upload_to='media', blank=True)
