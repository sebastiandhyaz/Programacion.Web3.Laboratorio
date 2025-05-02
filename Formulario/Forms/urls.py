from django.urls import path
from .views import nuevo_usuario
from .views import usuarios  # Importar la vista usuarios

urlpatterns = [
    path('nuevo_usuario/', nuevo_usuario, name='nuevo_usuario'),  # Ruta para nuevo_usuario
    path('usuarios/', usuarios, name='usuarios'),  # Nueva ruta para usuarios
]
