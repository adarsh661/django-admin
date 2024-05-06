from django.db import models

# Create your models here.from django.db import models
class Education(models.Model):
    qualification= models.CharField(max_length=100,null=True, blank=True)
    
    
    def __str__(self):
        return self.qualification 



class Profile(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
       
    ]
    name = models.CharField(max_length=100)
    image= models.ImageField(upload_to='profileimage', null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    address = models.CharField(max_length=200,null=True, blank=True)
    phone = models.CharField(max_length=15,null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,null=True, blank=True)
    education = models.ManyToManyField(Education)
    
    
    
    def __str__(self):
        return self.name       
    
class Product(models.Model):
    
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    address = models.CharField(max_length=200,null=True, blank=True)
    phone = models.CharField(max_length=15,null=True, blank=True)
    
    def __str__(self):
        return self.name 
    
    
class Person(models.Model):
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=200,null=True, blank=True)
    height = models.CharField(max_length=200,null=True, blank=True)
    weight = models.CharField(max_length=200,null=True, blank=True)
    
    def __str__(self):
        return self.name 
    
    
