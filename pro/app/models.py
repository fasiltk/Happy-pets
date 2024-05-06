from django.db import models
#Create your models here.
class Users(models.Model):
    username=models.CharField(max_length=244)
    password=models.CharField(max_length=244)
    name=models.CharField(max_length=244)
    phonenumber=models.CharField(max_length=10)
    role=models.CharField(max_length=10,null=True)
    def __str__(self):
        return f"{self.name}"
class Pets(models.Model):
    pet_name=models.CharField(max_length=244)
    description=models.CharField(max_length=1000)
    age=models.FloatField()
    food=models.CharField(max_length=250)
    medical=models.CharField(max_length=500)
    price=models.IntegerField()
    image=models.ImageField(upload_to='images/')
    def __str__(self):
        return f"{self.pet_name}"
class Buy(models.Model):
    pet_name=models.CharField(max_length=244)
    description=models.CharField(max_length=1000)
    image=models.ImageField(upload_to='images/')
    username=models.CharField(max_length=244,null=True)
    def __str__(self):
        return f"{self.pet_name}"
class Confirm(models.Model):
    pet_name=models.CharField(max_length=244)
    description=models.CharField(max_length=1000)
    image=models.ImageField(upload_to='images/')
    username=models.CharField(max_length=244,null=True)
    def __str__(self):
        return f"{self.pet_name}"
class ChatUser(models.Model):
    usr=models.CharField(max_length=244)
    message=models.TextField()
class ChatManager(models.Model):
    usr=models.CharField(max_length=244)
    usruser=models.CharField(max_length=244)
    message=models.TextField()