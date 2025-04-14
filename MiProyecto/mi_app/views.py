from django.shortcuts import render
from django.http import HttpResponse

def saludo(request):
    return HttpResponse("¡Hola, bienvenido a mi proyecto Django!")

