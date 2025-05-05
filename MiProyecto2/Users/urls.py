from django.urls import path
from . import views

urlpatterns = [
    path("listado_usuarios/", views.listado_usuarios, name="listado_usuarios"),  # Ruta para listar usuarios
]