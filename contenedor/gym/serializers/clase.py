# gym/serializers.py
from rest_framework import serializers
from ..models.clase import Clase
from .entrenador import EntrenadorSerializer

class ClaseSerializer(serializers.ModelSerializer):
    entrenador = EntrenadorSerializer()

    class Meta:
        model = Clase
        fields = ['id', 'nombre', 'horario', 'capacidad', 'entrenador', 'precio']