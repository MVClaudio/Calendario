from django.contrib import admin
from .models import Evento,Feriado,Usuario
# Register your models here.

admin.site.register(Usuario)
admin.site.register(Evento)
admin.site.register(Feriado)