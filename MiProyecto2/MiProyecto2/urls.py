"""
URL configuration for MiProyecto2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse("Bienvenido a MiProyecto2. Ve a /admin para el panel de administración.")

urlpatterns = [
    path("", home, name="home"),  # Ruta para la página principal
    path("admin/", admin.site.urls),
    # Aquí puedes agregar rutas adicionales si las aplicaciones tienen sus propias URLs.
]
