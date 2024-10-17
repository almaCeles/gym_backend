from rest_framework import generics
from drf_yasg.utils import swagger_auto_schema
from django.db.models import Prefetch

from ..models.clase import Clase
from ..models.entrenador import Entrenador
from ..serializers.entrenador import EntrenadorSerializer, EntrenadorDetallesSerializer

class EntrenadorListCreate(generics.ListCreateAPIView):
    queryset = Entrenador.objects.all()
    serializer_class = EntrenadorSerializer

    @swagger_auto_schema(
        operation_description="Obtiene la lista de entrenadores o crea uno nuevo.",
        responses={200: EntrenadorSerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        request_body=EntrenadorSerializer,
        responses={201: EntrenadorSerializer}
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class EntrenadorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Entrenador.objects.all()
    serializer_class = EntrenadorSerializer

class EntrenadorList(generics.ListAPIView):
    serializer_class = EntrenadorDetallesSerializer

    def get_queryset(self):
        return Entrenador.objects.prefetch_related(
            Prefetch(
                'clases',
                queryset= Clase.objects.prefetch_related('reservas')
            )
        )