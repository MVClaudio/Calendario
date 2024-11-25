from django import forms
from .models import Evento,Feriado
from django.core.exceptions import ValidationError

class EventoForm(forms.ModelForm):
    class Meta:
        model=Evento
        fields=["titulo","descripcion","fecha_inicio","fecha_fin","tipo_evento","estado"]
        widgets={
            "fecha_inicio":forms.DateInput(attrs={"type":"date"}),
            "fecha_fin":forms.DateInput(attrs={"type":"date"})
        }

    def clean(self):
        cleaned_data=super().clean()
        fecha_inicio= cleaned_data.get("fecha_inicio")
        fecha_fin= cleaned_data.get("fecha_fin")
        
        if fecha_inicio and fecha_fin:
            if fecha_inicio>fecha_fin:
                raise ValidationError("La fecha de inicio no puede ser mayor a la de termino ")
            
            feriados= Feriado.objects.filter(fecha__range=(fecha_inicio,fecha_fin))
            if feriados.exists():
                feriado_existe= feriados.first()
                raise ValidationError(f"El evento coincide con el feriado {feriado_existe.nombre} el {feriado_existe.fecha}. Verifica las fechas.")
        

    def clean_title(self):
        titulo= self.cleaned_data.get("titulo")
        if Evento.objects.filter(titulo=titulo).exists():
            raise ValidationError(f"Ya existe un evento con el titulo {titulo}.")
        return titulo