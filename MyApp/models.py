from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    genero = models.CharField(max_length=30)
    creador = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.nombre} by {self.creador}'

class Desarrollador(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.nombre}'

class Comprador(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Vendedor(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()

    def __str__(self):
        return f'{self.nombre} {self.apellido}'