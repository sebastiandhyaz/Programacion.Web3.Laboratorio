from django.urls import path
from . import views

urlpatterns = [
    path('coment/', views.coment, name='coment'),
    path('verificar-numero/<int:numero>/', views.verificar_numero, name='verificar_numero'),
    path("vista-parametrizada/", views.mostrar_datos, name="vista-parametrizada"),  # Cambiado a 'mostrar_datos'
]