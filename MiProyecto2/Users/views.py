from django.shortcuts import render
from django.contrib.auth.models import User  # Importar el modelo User

def listado_usuarios(request):
    usuarios = User.objects.all()  # Obtener todos los usuarios
    return render(request, "users/listado_usuarios.html", {"usuarios": usuarios})