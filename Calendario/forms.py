from django import forms
from .models import Evento

class EventoForm(forms.ModelForm):
    class Meta:
        model=Evento
        fields=["titulo","descripcion","fecha_inicio","fecha_fin","tipo_evento","estado"]