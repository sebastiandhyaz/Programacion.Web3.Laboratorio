from django.shortcuts import render
from .models import Computadora

def listado_computadoras(request):
    computadoras = Computadora.objects.all()
    return render(request, 'computadora/listado_computadoras.html', {'computadoras': computadoras})

