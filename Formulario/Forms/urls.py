from django.urls import path
from .views import nuevo_usuario

urlpatterns = [
    path('nuevo_usuario/', nuevo_usuario, name='nuevo_usuario'),  # Ruta para nuevo_usuario
]
