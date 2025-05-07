
from django.contrib import admin
from django.urls import path, include

# from principal import views as principal_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('computadora.urls') ),
    
]


