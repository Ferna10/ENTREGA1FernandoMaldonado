from atexit import register
from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Inicio)
admin.site.register(Clientes)
admin.site.register(Turnos)
admin.site.register(Autos)
admin.site.register(Operacion)
