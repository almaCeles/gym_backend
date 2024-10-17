from rest_framework import generics
from ..models.reserva import Reserva
from ..serializers.reserva import ReservaSerializer


class ReservaListCreate(generics.ListCreateAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer