from rest_framework import generics
from rest_framework.response import Response
from ..models.cliente import Cliente
from ..models.reserva import Reserva
from ..serializers.cliente import ClienteSerializer
from ..serializers.clase import ClaseInscritaSerializer

class ClienteListCreate(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    
class  ClienteRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class ClienteClasesView(generics.GenericAPIView):
    serializer_class = ClaseInscritaSerializer

    def get(self, request, pk):
        try:
            cliente = Cliente.objects.get(pk=pk)
        except Cliente.DoesNotExist:
            return Response({'error': 'Cliente no encontrado'}, status=404)

        reservas = Reserva.objects.filter(cliente=cliente)

        clases = [reserva.clase for reserva in reservas]

        serializer = self.get_serializer(clases, many=True)

        # Retornar la respuesta con la cantidad de clases y los detalles de las clases
        return Response({
            'cliente': cliente.nombre,
            'cantidad_clases': len(clases),
            'clases': serializer.data
        })