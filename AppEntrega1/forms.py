from django import forms

# Create your models here.

class Clientes(forms.Form):
    nombre=forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email= forms.EmailField()
    telefono=forms.IntegerField()

class ClientesForms(forms.Form):
    nombre=forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email= forms.EmailField()
    telefono=forms.IntegerField()

class TurnosForms(forms.Form):
    fecha= forms.DateField()
    hora = forms.CharField(max_length=8)

class AutosForms(forms.Form):
    marca=forms.CharField(max_length=30)
    modelo=forms.CharField(max_length=30)
    kilometraje=forms.IntegerField()
    motor=forms.CharField(max_length=30)

class OperacionForms(forms.Form):
    mantenimiento=forms.CharField(max_length=30)
    reparacion=forms.CharField(max_length=30)
    diagnostico=forms.CharField(max_length=30)



