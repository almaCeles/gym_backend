from django.db import models

class Entrenador(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre