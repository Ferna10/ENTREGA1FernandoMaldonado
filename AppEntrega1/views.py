from django import http
from django.shortcuts import render
from django.http import HttpResponse
from AppEntrega1.models import Inicio, Clientes, Turnos, Autos, Operacion  
from AppEntrega1.forms import ClientesForms, TurnosForms, AutosForms, OperacionForms
# Create your views here.
def inicio(request):
    return render(request,"AppEntrega1/inicio.html")

def clientes(request):
    return render(request,"AppEntrega1/clientes.html")

def turnos(request):
    return render(request,"AppEntrega1/turnos.html")

def autos(request):
    return render(request,"AppEntrega1/autos.html")

def operacion(request):
    return render(request,"AppEntrega1/operacion.html")



def clientes_formulario(request):
    if (request.method =="POST"):
        formulario=ClientesForms(request.POST)
        print(formulario)
        
        if formulario.is_valid:
            informacion= formulario.cleaned_data
            print(informacion)
            nombre=informacion["nombre"]
            apellido=informacion["apellido"]
            email=informacion["email"]
            telefono=informacion["telefono"]
            clientes= Clientes(nombre=nombre, apellido=apellido, email=email, telefono=telefono)
            clientes.save()
            return render(request,"AppEntrega1/cliente.html")
    else:
        formulario= ClientesForms()
    return render(request,'AppEntrega1/clientes_formulario.html/',{"formulario":formulario})


def autos_formulario(request):
    if (request.method=="POST"):
        formulario=AutosForms(request.POST)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            marca=informacion["marca"]
            modelo=informacion["modelo"]
            kilometraje=informacion["kilometraje"]
            motor=informacion["motor"]
            autos=Autos(marca=marca, modelo=modelo, kilometraje=kilometraje, motor=motor)
            autos.save()
            return render(request,"AppEntrega1/autos.html/")
    else:
        formulario=AutosForms()
    return render(request,"AppEntrega1/autos_formulario.html",{"formulario":formulario})

def turnos_formulario(request):
    if (request.method=="POST"):
        formulario=TurnosForms(request.POST)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            fecha=informacion["fecha"]
            hora=informacion["hora"]
            turnos=Turnos(fecha=fecha,hora=hora)
            turnos.save()
            return render(request,"AppEntrega1/turnos.html/")
    else:
        formulario=TurnosForms()
    return render(request,"AppEntrega1/turnos_formulario.html",{"formulario":formulario})


def operacion_formulario(request):
    if (request.method=="POST"):
        formulario=OperacionForms(request.POST)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            mantenimiento=informacion["mantenimiento"]
            reparacion=informacion["reparacion"]
            diagnostico=informacion["diagnostico"]
            operacion=Operacion(mantenimiento=mantenimiento, reparacion=reparacion, diagnostico=diagnostico)
            operacion.save()
            return render(request,"AppEntrega1/operacion.html/")
    else:
        formulario=OperacionForms()
    return render(request,"AppEntrega1/operacion_formulario.html",{"formulario":formulario})
      

