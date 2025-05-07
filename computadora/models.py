from django.db import models
from django.contrib.auth.models import User

# MODELO COMPUTADORA 

class Computadora(models.Model):
    modelo = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    cap_hd = models.FloatField()   
    cap_ram = models.FloatField()  
    precio = models.FloatField()   
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  

    def __str__(self):
        return f"{self.marca} {self.modelo}"
