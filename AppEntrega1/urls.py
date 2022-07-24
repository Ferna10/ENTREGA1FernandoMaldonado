from django.urls import path
from .views import *



urlpatterns = [ 
    path ('inicio/', inicio, name='inicio'),
    path ('clientes/',clientes, name='clientes'),
    path ('turnos/',turnos, name='turnos'),
    path ('autos/',autos, name='autos'),
    path ('operacion/',operacion, name='operacion'),
    path ('clientes_formulario/',clientes_formulario, name='clientes_formulario'),
    path ('turnos_formulario/',turnos_formulario, name='turnos_formulario'),
    path ('autos_formulario/',autos_formulario, name='autos_formulario'),
    path ('operacion_formulario/',operacion_formulario, name='operacion_formulario'),

]

