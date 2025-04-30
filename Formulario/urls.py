from django.contrib import admin
from django.urls import path, include  # Importar include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('forms/', include('Formulario.Forms.urls')),  # Incluir las rutas de Forms
]
