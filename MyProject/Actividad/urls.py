from django.urls import path
from .views import InicioView

urlpatterns = [
    path('', InicioView.as_view(), name='Nombre_completo'),
]
