from rest_framework import generics
from ..models.clase import Clase

from ..serializers.clase import  ClaseSerializer

class ClaseListCreate(generics.ListCreateAPIView):
    queryset = Clase.objects.all()
    serializer_class = ClaseSerializer
