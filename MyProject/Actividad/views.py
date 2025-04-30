from django.shortcuts import render
from datetime import date
from django.views.generic import TemplateView
from .forms import ActividadForm

class InicioView(TemplateView):
    template_name = 'Actividad/inicio.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nombre_completo'] = "SEBASTIAN ENRIQUE DIAZ DE OROPEZA NINA"
        context['carnet'] = "14226785"
        context['fecha_hoy'] = date.today().strftime("%d/%m/%Y")
        return context

def actividad_view(request):
    if request.method == 'POST':
        form = ActividadForm(request.POST)
        if form.is_valid():
            # Procesar los datos del formulario
            return render(request, 'actividad_success.html', {'form': form})
    else:
        form = ActividadForm()
    return render(request, 'actividad_form.html', {'form': form})

def actividad_menu(request):
    return render(request, 'Actividad/menu.html')
