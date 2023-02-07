from django.urls import path
from .views import *

#PASAR EL INICIO AL OTRO URLS PARA QUE QUEDE EL BODY EN LA PAGINA PRINCIPAL Y LOS BOTONES REDIRECCIONEN A LA APP

urlpatterns = [
    path('fabrica', fabrica),
    path('modelo', modelo),
    path('ensamblador', ensamblador),
    path('', inicio),
]