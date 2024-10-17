from rest_framework import serializers
from ..models.entrenador import Entrenador

class EntrenadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entrenador
        fields = ['id', 'nombre', 'especialidad']

class EntrenadorSerializerResumen(serializers.ModelSerializer):
    clases = serializers.SerializerMethodField()

    class Meta:
        model = Entrenador
        fields = ['id', 'nombre', 'especialidad', 'clases'] 

    def get_clases(self, obj):
        from .clase import ClaseSerializer  
        return ClaseSerializer(obj.clases.all(), many=True).data  
    
class EntrenadorDetallesSerializer(serializers.ModelSerializer):
    clases = serializers.SerializerMethodField() 

    class Meta:
        model = Entrenador
        fields = ['nombre', 'especialidad', 'clases']
    
    def get_clases(self, obj):
        from ..serializers.clase import ClaseClienteSerializer  
        clases = obj.clases.prefetch_related('reservas')
        return ClaseClienteSerializer(clases, many=True).data