from rest_framework import serializers
from Calendario.models import Evento,Feriado

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Evento
        fields="__all__"

class FeriadoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Feriado
        fields= "__all__"

class CalendarioSerializer(serializers.ModelSerializer):
    EventoSerializer()
    FeriadoSerializer()
    