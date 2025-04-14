from django.urls import path
from Comentarios import views as Comentarios_views

urlpatterns = [
    path('coment/', Comentarios_views.coment, name='coment'),
    path("verifica-numero/<int:numero>/", Comentarios_views.verificar_numero, name='verificar_numero'),  # Corregido
    path("vista-parametrizada/", Comentarios_views.recibe_param, name="vista-parametrizada")
]