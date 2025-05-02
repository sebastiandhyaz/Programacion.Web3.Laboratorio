from django.db import models
from django.contrib.auth.models import User
from publicaciones.models import Publicacion

class Comentario(models.Model):
    contenido = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE)
    fecha_creacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.autor} en {self.publicacion}"

    class Meta:
        db_table = "comentarios"  # Define el nombre de la tabla como "comentarios"
