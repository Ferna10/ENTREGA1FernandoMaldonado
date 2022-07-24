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
    
    def __str__(self):
        return self.nombre+" "+self.apellido+" "+self.email+" "+str(self.telefono)

class Turnos(models.Model):
    fecha= models.DateField()
    hora= models.TimeField()

    def __str__(self):
        return str(self.fecha)+" "+str(self.hora)

class Autos(models.Model):
    marca=models.CharField(max_length=30)
    modelo=models.CharField(max_length=30)
    kilometraje=models.IntegerField()
    motor=models.CharField(max_length=30)
    
    def __str__(self):
        return self.marca+" "+self.modelo+" "+str(self.kilometraje)+" "+self.motor


class Operacion(models.Model):
    mantenimiento=models.CharField(max_length=30)
    reparacion=models.CharField(max_length=30)
    diagnostico=models.CharField(max_length=30)
    
    def __str__(self):
        return self.mantenimiento+" "+self.reparacion+" "+self.diagnostico




