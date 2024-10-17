# gym/serializers.py
from rest_framework import serializers
from ..models.reserva import Reserva
from .clase import ClaseSerializer
from .cliente import ClienteSerializer

class ReservaSerializer(serializers.ModelSerializer):
    clase = ClaseSerializer()
    cliente = ClienteSerializer()

    class Meta:
        model = Reserva
        fields = ['id', 'clase', 'cliente', 'fecha_reserva']