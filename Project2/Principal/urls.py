from django.urls import path
from . import views

urlpatterns = [
    path('saludo/', views.saludo, name='saludo'),
    path('SaludoAvanzado/', views.SaludoAvanzado.as_view(), name='saludo-avanzado'),
    path('VistaParametrizada/', views.VistaParametrizada.as_view(), name='vista-parametrizada')
]
