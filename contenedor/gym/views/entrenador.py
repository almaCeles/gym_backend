from rest_framework import generics
from ..models.entrenador import Entrenador
from ..serializers.entrenador import EntrenadorSerializer

class EntrenadorListCreate(generics.ListCreateAPIView):
    queryset = Entrenador.objects.all()
    serializer_class = EntrenadorSerializer
