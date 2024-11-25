from django.shortcuts import render
from rest_framework import viewsets
from Calendario.models import Feriado,Evento
from .serializers import EventoSerializer,FeriadoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

# class modeloViewSet(viewsets.ModelViewSet):

class EventoViewSet(viewsets.ModelViewSet):
    queryset=Evento.objects.all()
    serializer_class=EventoSerializer

class FeriadoViewSet(viewsets.ModelViewSet):
    queryset=Feriado.objects.all()
    serializer_class=FeriadoSerializer


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
            calendario.append({"evento":EventoSerializer(evento).data})
        for feriado in feriados:
            calendario.append({"feriado":FeriadoSerializer(feriado).data})
        
        calendario.sort(key=obtener_fecha)
        return Response(calendario)