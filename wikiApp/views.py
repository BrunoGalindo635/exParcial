from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.

def vista_principal(request):
    return HttpResponse("Vista principal")

def crear_tema(request):
    return HttpResponse("Crear nuevo tema")

def crear_articulo(request):
    return HttpResponse("Crear nuevo artículo")

def articulos_por_tema(request, tema_id):
    return HttpResponse(f"Artículos del tema {tema_id}")

def ver_articulo(request, articulo_id):
    return HttpResponse(f"Ver artículo {articulo_id}")

def buscar_articulos(request):
    return HttpResponse("Buscar artículos")