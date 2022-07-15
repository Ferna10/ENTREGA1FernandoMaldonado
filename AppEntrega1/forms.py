from django import forms

class ClienteForm(forms.Form):
    nombre=forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email= forms.EmailField()
    solicitud=forms.CharField(max_length=30)

class AtencionClientesForm(forms.Form):
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    telefono=forms.IntegerField()
    turno=forms.CharField(max_length=30)

class AutoForm(forms.Form):
    condicion=forms.CharField(max_length=30)
    modelo=forms.CharField(max_length=30)
    kilometraje=forms.IntegerField()
    tipo = forms.CharField(max_length=30)
    precio=forms.IntegerField()


class MecanicoForm(forms.Form):
    nombre=forms.CharField(max_length=30)
    apellido=forms.CharField(max_length=30)
    categoria=forms.CharField(max_length=30)
    trabajo=forms.CharField(max_length=30)
