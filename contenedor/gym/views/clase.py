from rest_framework import generics

from django.db.models import Count

from ..models.clase import Clase
from ..serializers.clase import  ClaseSerializer, ClaseSerializerReservaCount

class ClaseListCreate(generics.ListCreateAPIView):
    queryset = Clase.objects.all()
    serializer_class = ClaseSerializer

class ClaseRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Clase.objects.all()
    serializer_class = ClaseSerializer


class ClaseList(generics.ListAPIView):
    serializer_class = ClaseSerializerReservaCount

    def get_queryset(self):
        # Anotar cada clase con el número de reservas
        return Clase.objects.annotate(reserva_count=Count('reservas')).select_related('entrenador')

