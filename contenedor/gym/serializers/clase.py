# gym/serializers.py
from rest_framework import serializers
from ..models.clase import Clase
from ..models.reserva import Reserva
from .entrenador import EntrenadorSerializer
from ..serializers.cliente import ClienteNombreSerializer

class ClaseSerializer(serializers.ModelSerializer):
    #entrenador = EntrenadorSerializer()

    class Meta:
        model = Clase
        fields = ['id', 'nombre', 'horario', 'capacidad', 'entrenador', 'precio']

class ClaseSerializerReservaCount(serializers.ModelSerializer):
    reserva_count = serializers.IntegerField(read_only=True)
    entrenador = EntrenadorSerializer()
    
    class Meta:
        model = Clase
        fields = ['id', 'nombre', 'horario', 'capacidad', 'entrenador', 'precio', 'reserva_count']

class ClaseClienteSerializer(serializers.ModelSerializer):
    clientes = serializers.SerializerMethodField() 

    class Meta:
        model = Clase
        fields = ['nombre', 'horario', 'precio', 'clientes']

    def get_clientes(self, obj):

        # Obtiene las reservas de la clase y extrae los clientes
        reservas = Reserva.objects.filter(clase=obj)  # Filtrar por la clase
        clientes = [reserva.cliente for reserva in reservas]  # Extraer clientes de las reservas
        return ClienteNombreSerializer(clientes, many=True).data  # Serializar clientes

class ClaseInscritaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clase
        fields = ['nombre', 'horario', 'precio']