# gym/urls.py
from django.urls import path
from .views.entrenador import EntrenadorListCreate
from .views.clase import ClaseListCreate
from .views.cliente import  ClienteListCreate
from .views.reserva import ReservaListCreate

urlpatterns = [
    path('entrenadores/', EntrenadorListCreate.as_view(), name='entrenador-list-create'),
    path('clases/', ClaseListCreate.as_view(), name='clase-list-create'),
    path('clientes/', ClienteListCreate.as_view(), name='cliente-list-create'),
    path('reservas/', ReservaListCreate.as_view(), name='reserva-list-create'),
]
