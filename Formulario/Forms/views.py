from django.shortcuts import render
from .forms import FormularioNuevoUsuario

def nuevo_usuario(request):
    if request.method == 'POST':
        form = FormularioNuevoUsuario(request.POST)
        if form.is_valid():
            datos_contexto = {
                'nombre': form.cleaned_data['nombre'],
                'apellido': form.cleaned_data['apellido'],
                'fecha_nacimiento': f"{form.cleaned_data['fecha_dia']} de {form.cleaned_data['fecha_mes']} de {form.cleaned_data['fecha_anio']}",
                'genero': form.cleaned_data['genero'],
                'password': 'oculto',  # No mostrar la contraseña directamente
            }
            return render(request, 'principal/resumen_usuario.html', datos_contexto)
    else:
        form = FormularioNuevoUsuario()
    return render(request, 'principal/formulario_usuario.html', {'form': form})
