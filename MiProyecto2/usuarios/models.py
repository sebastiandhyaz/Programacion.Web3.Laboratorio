from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    codigo = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "usuarios"  # Define el nombre de la tabla como "usuarios"
