from django.shortcuts import render
from datetime import date
from django.views.generic import TemplateView

class InicioView(TemplateView):
    template_name = 'Actividad/inicio.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nombre_completo'] = "SEBASTIAN ENRIQUE DIAZ DE OROPEZA NINA"
        context['carnet'] = "14226785"
        context['fecha_hoy'] = date.today().strftime("%d/%m/%Y")
        return context
