from django.urls import path
from . import views

urlpatterns = [
    path("listado_publicaciones/", views.listado_publicaciones, name="listado_publicaciones"),  # Ruta para listar publicaciones
]
