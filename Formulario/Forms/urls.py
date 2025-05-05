from django.urls import path
from . import views  # Asegúrate de importar las vistas correctamente

urlpatterns = [
    path('nuevo_usuario/', views.nuevo_usuario, name='nuevo_usuario'),  # Ruta para nuevo_usuario
    path('usuarios/', views.usuarios, name='usuarios'),  # Corrige la referencia a la vista
]
