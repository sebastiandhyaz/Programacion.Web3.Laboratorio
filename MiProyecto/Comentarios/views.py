from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def coment(request):
    year = datetime.now().year
    return HttpResponse(f"¡Mi primer Comentario en Django! {year}")  # Usamos f-string

def verificar_numero(request, numero):
    if numero % 2 == 0:
        msg = "par"
    else:
        msg = "impar"
    return HttpResponse(msg)

def recibe_param(request, cadena, dato_num):
    # Usamos f-string para formatear la cadena correctamente
    return HttpResponse(f"Se recibió la cadena: {cadena} y el número: {dato_num}")

def nombre(request):
    return HttpResponse("¡Hola, este es el mensaje desde la vista 'nombre'!")