from django.db import models

# Create your models here.

class Fabrica(models.Model):
    nombre = models.CharField(max_length=50)

class Modelo(models.Model):
    nombre = models.CharField(max_length=50)
    patente =  models.IntegerField()
    color = models.CharField(max_length=50)
    vendido = models.BooleanField()

class Ensamblador(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()


