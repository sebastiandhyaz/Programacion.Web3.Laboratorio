from django.shortcuts import render
from .forms import FormularioNuevoUsuario

# Asegúrate de que 'usuarios' esté definido o importado correctamente
# Si 'usuarios' es una función o variable, defínela o impórtala desde el módulo correcto
# Ejemplo de definición:
usuarios = []  # Si 'usuarios' es una lista o colección

# Si 'usuarios' debe ser importado desde otro archivo, corrige la importación:
# from .otro_modulo import usuarios

def nuevo_usuario(request):
    if request.method == 'POST':
        form = FormularioNuevoUsuario(request.POST)
        if form.is_valid():
            # Extraer datos del formulario
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            fecha_dia = form.cleaned_data['fecha_dia']
            fecha_mes = form.cleaned_data['fecha_mes']
            fecha_anio = form.cleaned_data['fecha_anio']
            genero = form.cleaned_data['genero']
            email = form.cleaned_data['email']
            aficiones = form.cleaned_data['aficiones']
            password = form.cleaned_data['password']

            # Formatear fecha de nacimiento
            fecha_nacimiento = f"{fecha_dia} de {fecha_mes} de {fecha_anio}"

            # Renderizar la plantilla de resumen con los datos
            return render(request, 'principal/resumen_usuario.html', {
                'nombre': nombre,
                'apellido': apellido,
                'fecha_nacimiento': fecha_nacimiento,
                'genero': genero,
                'email': email,
                'aficiones': aficiones,
                'password': password
            })
        else:
            # Si hay errores, renderizar el formulario con los errores
            return render(request, 'principal/formulario_usuario.html', {'form': form})
    else:
        # Renderizar el formulario vacío en solicitudes GET
        form = FormularioNuevoUsuario()
        return render(request, 'principal/formulario_usuario.html', {'form': form})

def usuarios(request):
    # Lógica para manejar la vista de usuarios
    return render(request, 'principal/usuarios.html')  # Asegúrate de tener esta plantilla
