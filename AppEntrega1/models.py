from django.db import models

# Create your models here.
class Inicio(models.Model):
    nombre=models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email= models.EmailField()
    telefono=models.IntegerField()

class Clientes(models.Model):
    nombre=models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email= models.EmailField()
    telefono=models.IntegerField()

class Turnos(models.Model):
    fecha= models.DateTimeField()
    hora= models.CharField(max_length=10)

class Autos(models.Model):
    marca=models.CharField(max_length=30)
    modelo=models.CharField(max_length=30)
    kilometraje=models.IntegerField()
    motor=models.CharField(max_length=30)

class Operacion(models.Model):
    mantenimiento=models.CharField(max_length=30)
    reparacion=models.CharField(max_length=30)
    diagnostico=models.CharField(max_length=30)



