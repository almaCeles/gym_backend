from rest_framework import generics
from ..models.cliente import Cliente

from ..serializers.cliente import ClienteSerializer


class ClienteListCreate(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer