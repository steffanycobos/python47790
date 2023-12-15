from django.db import models
from django.contrib.auth.models import User
from  django.utils.timezone import now


class Products(models.Model):
    title= models.CharField(max_length=50)
    description= models.CharField(max_length=100)
    price= models.IntegerField()
    stock=models.IntegerField()
    imagen= models.ImageField( upload_to='media/', null=True, blank=True)
    


class Avatar(models.Model):
 user= models.OneToOneField(User, on_delete= models.CASCADE)
 imagen= models.ImageField( upload_to='media/avatar', null=True, blank=True)

 def __str__(self):
     return f'{self.user}, {self.imagen}'