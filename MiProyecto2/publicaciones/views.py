from django.shortcuts import render
from .models import Publicacion

def listado_publicaciones(request):
    publicaciones = Publicacion.objects.all()  # Obtener todas las publicaciones
    return render(request, "publicaciones/listado_publicaciones.html", {"publicaciones": publicaciones})
