from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre=models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email= models.EmailField()
    solicitud=models.CharField(max_length=30)

class AtencionClientes(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    telefono=models.IntegerField()
    turno=models.CharField(max_length=30)

class Auto(models.Model):
    condicion=models.CharField(max_length=30)
    modelo=models.CharField(max_length=30)
    kilometraje=models.IntegerField()
    tipo = models.CharField(max_length=30)
    precio=models.IntegerField()


class Mecanico(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    categoria=models.CharField(max_length=30)
    trabajo=models.CharField(max_length=30)


