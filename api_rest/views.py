from django.shortcuts import render
from rest_framework import viewsets,filters
from django_filters.rest_framework import DjangoFilterBackend
from Calendario.models import Feriado,Evento
from .serializers import EventoSerializer,FeriadoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

# class modeloViewSet(viewsets.ModelViewSet):

class EventoViewSet(viewsets.ModelViewSet):
    queryset=Evento.objects.all()
    serializer_class=EventoSerializer
    filter_backends=[DjangoFilterBackend,filters.OrderingFilter]
    filterset_fields=["tipo_evento","fecha_inicio"]
    ordering_fields=["fecha_inicio"]

class FeriadoViewSet(viewsets.ModelViewSet):
    queryset=Feriado.objects.all()
    serializer_class=FeriadoSerializer
    filter_backends=[DjangoFilterBackend]
    filterset_fields=["tipo","fecha"]


def obtener_fecha(obj):
    if "evento" in obj:
        return obj["evento"]["fecha_inicio"]
    elif "feriado" in obj:
        return obj["feriado"]["fecha"]

class CalendarioViewSet(APIView):
    def get(self,request):
        eventos=Evento.objects.all()
        feriados=Feriado.objects.all()

        calendario=[]
        for evento in eventos:
            evento_data= EventoSerializer(evento).data
            evento_data.pop("id",None)
            calendario.append({"evento":evento_data})
        for feriado in feriados:
            feriado_data=FeriadoSerializer(feriado).data
            feriado_data.pop("id",None)
            calendario.append({"feriado":feriado_data})
            
        
        calendario.sort(key=obtener_fecha)
        return Response(calendario)