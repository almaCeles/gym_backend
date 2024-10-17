# gym/serializers.py
from rest_framework import serializers
from ..models.cliente import Cliente



class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nombre', 'correo', 'membresia']


class ClienteNombreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['nombre']