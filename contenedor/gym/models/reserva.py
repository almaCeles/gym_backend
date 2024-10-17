from django.db import models
from .clase import Clase
from .cliente import Cliente

class Reserva(models.Model):
    clase = models.ForeignKey(Clase, on_delete=models.CASCADE, related_name='reservas')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='reservas')
    fecha_reserva = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Reserva de {self.cliente} para la clase {self.clase}'