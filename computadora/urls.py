from django.urls import path
from . import views

urlpatterns = [
    path('lista_computadoras/', views.listado_computadoras, name='listado_computadoras'),
]
