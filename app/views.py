from django.shortcuts import render
from .models import Fabrica
from django.http import HttpResponse

# Create your views here.

def fabrica(request):
    fabrica1= Fabrica(nombre="ford")
    fabrica1.save()
    cadena_texto=f"fabrica guardada: Nombre: {fabrica1.nombre}."
    return HttpResponse(cadena_texto)

def modelo(request):
    return render (request, "app/modelo.html")

def ensamblador(request):
    return render (request, "app/ensamblador.html")

def inicio(request):
    return render (request, "app/inicio.html")