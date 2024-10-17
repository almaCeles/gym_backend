from django.db import models
from .entrenador import Entrenador

class Clase(models.Model):
    nombre = models.CharField(max_length=100)
    horario = models.DateTimeField()
    capacidad = models.PositiveIntegerField()
    entrenador = models.ForeignKey(Entrenador, on_delete=models.CASCADE, related_name='clases')
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre