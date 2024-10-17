# gym/urls.py
from django.urls import path
from .views.entrenador import EntrenadorListCreate, EntrenadorRetrieveUpdateDestroy, EntrenadorList
from .views.clase import ClaseListCreate, ClaseRetrieveUpdateDestroy, ClaseList
from .views.cliente import  ClienteListCreate , ClienteRetrieveUpdateDestroy, ClienteClasesView
from .views.reserva import ReservaListCreate , ReservaRetrieveUpdateDestroy, ReservasPorDiaView

urlpatterns = [
    path('entrenadores/', EntrenadorListCreate.as_view(), name='entrenador-list-create'),
    path('entrenadores/<int:pk>/', EntrenadorRetrieveUpdateDestroy.as_view(), name='entrenador-'),
    path('entrenadores-detalle/', EntrenadorList.as_view(), name='entrenador-detail'),

    path('clases/', ClaseListCreate.as_view(), name='clase-list-create'),
    path('clases/<int:pk>/', ClaseRetrieveUpdateDestroy.as_view(), name='clases-detail'),
    path('clases-reservadas_all/', ClaseList.as_view(), name='clase-list'),

    path('clientes/', ClienteListCreate.as_view(), name='cliente-list-create'),
    path('clientes/<int:pk>/', ClienteRetrieveUpdateDestroy.as_view(), name='cliente-detail'),
    path('cliente/<int:pk>/clases/', ClienteClasesView.as_view(), name='cliente-clases'),

    path('reservas/', ReservaListCreate.as_view(), name='reserva-list-create'),
    path('reservas/<int:pk>/', ReservaRetrieveUpdateDestroy.as_view(), name='reserva-detail'),
    path('reservas/<str:fecha>/', ReservasPorDiaView.as_view(), name='reservas-por-dia'),
]
