from django.contrib import admin
from django.urls import path, include
from mi_app import views as mi_app_views
from Comentarios import views as Comentarios_views

urlpatterns = [
    path("admin/", admin.site.urls, name='admin'),
    path('', include('Comentarios.urls'), name='comentarios'),  # Corregido: usamos include para las URLs de 'Comentarios'
    path('nombre/', mi_app_views.saludo, name='nombre'),  # Cambiado de 'saludo' a 'nombre'
    path('coment/', Comentarios_views.coment, name='coment'),
    path("verifica-numero/<int:numero>/", Comentarios_views.verificar_numero, name='verificar_numero'),
    path("vista-parametrizada/", Comentarios_views.mostrar_datos, name="vista-parametrizada"),
]
