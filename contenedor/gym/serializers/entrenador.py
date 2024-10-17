from rest_framework import serializers
from ..models.entrenador import Entrenador

class EntrenadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entrenador
        fields = ['id', 'nombre', 'especialidad']