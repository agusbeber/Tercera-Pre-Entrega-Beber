from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    genero = models.CharField(max_length=30)
    creador = models.CharField(max_length=30)

class Desarrollador(models.Model):
    nombre = models.CharField(max_length=30)

class Comprador(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()

class Vendedor(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()