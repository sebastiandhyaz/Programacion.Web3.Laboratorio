from django.db import models
from django.contrib.auth.models import User

class Publicacion(models.Model):  # Cambiado a singular
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo

    class Meta:
        db_table = "publicaciones"  # Define el nombre de la tabla como "publicaciones"
