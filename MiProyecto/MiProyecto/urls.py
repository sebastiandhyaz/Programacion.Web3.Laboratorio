from django.contrib import admin
from django.urls import path, include
from mi_app import views as mi_app_views
from Comentarios import views as Comentarios_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('Comentarios.urls')),  # Corregido: usamos include para las URLs de 'Comentarios'
    path('saludo/', mi_app_views.saludo, name='saludo'),
    #pah('coment/', Comentarios_views.coment, name='coment'),
    #pth("verifica-numero/<int:numero>/", Comentarios_views.verificar_numero, name='verificar_numero'),
    #pth("vista-parametrizada/", Comentarios_views.recibe_param, name="vista-parametrizada"),
]
