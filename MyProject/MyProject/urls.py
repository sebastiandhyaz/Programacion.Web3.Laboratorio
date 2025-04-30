from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('actividad/', include('Actividad.urls')),  # Incluye las URLs de la app Actividad
]
