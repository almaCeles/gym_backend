from rest_framework import generics
from ..models.reserva import Reserva
from ..serializers.reserva import ReservaSerializer
from rest_framework import generics
from rest_framework.response import Response
from django.utils import timezone
from ..models.reserva import Reserva
from ..serializers.reserva import ReservaPorDiaSerializer
from django.db.models import Q


class ReservaListCreate(generics.ListCreateAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

    
class ReservaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer



class ReservasPorDiaView(generics.GenericAPIView):
    serializer_class = ReservaPorDiaSerializer

    def get(self, request, fecha):
        try:
            fecha_dia = timezone.datetime.strptime(fecha, '%Y-%m-%d').date()

            # Filtrar reservas por fecha de la clase o la fecha de reserva
            reservas = Reserva.objects.filter(Q(fecha_reserva__date=fecha_dia) | Q(clase__horario__date=fecha_dia))

            # Serializar las reservas encontradas
            serializer = self.get_serializer(reservas, many=True)

            # Retornar la respuesta con las reservas del día
            return Response({
                'fecha': fecha_dia,
                'cantidad_reservas': reservas.count(),
                'reservas': serializer.data
            })

        except ValueError:
            return Response({'error': 'Formato de fecha no válido. Use YYYY-MM-DD'}, status=400)
