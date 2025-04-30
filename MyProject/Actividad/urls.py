from django.urls import path
from .views import InicioView, actividad_view, actividad_menu

urlpatterns = [
    path('', actividad_menu, name='actividad_menu'),  # Menú principal
    path('inicio/', InicioView.as_view(), name='inicio'),  # Página de inicio
    path('formulario/', actividad_view, name='actividad'),  # Página del formulario
]
