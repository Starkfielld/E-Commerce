from django.db import models

# Create your models here.
class Login(models.Model):
    login = models.CharField(max_length = 20)
    passoword = models.CharField(max_length=20)

class produto(models.Model):
    nameprod = models.CharField(max_length = 20)
    preco = models.FloatField(10)

class cliente(models.Model):
    nome = models.CharField( max_length=50)