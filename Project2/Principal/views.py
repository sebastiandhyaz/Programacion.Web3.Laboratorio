from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.

def saludo(request):
    return HttpResponse("¡Hola, este es un mensaje de saludo desde Principal!")

class SaludoAvanzado(TemplateView):
    template_name = "index.html"

class VistaParametrizada(TemplateView):
    template_name = "lista.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        nombre = self.kwargs.get('nombre', 'Juan')
        año = self.kwargs.get('año', 2024)
        edad = self.kwargs.get('edad', 30)
        
        nombreMayusculas = nombre.upper()
        
        context['nombre'] = nombreMayusculas
        context['año'] = año
        context['edad'] = edad
        return context
