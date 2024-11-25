from django.shortcuts import render,redirect
from .models import  Evento,Feriado
from .forms import EventoForm
from django.contrib import messages
import requests
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.utils.dateparse import parse_date

# Create your views here.

def obtener_feriados():
    headers = {
    'User-Agent': 'Mozilla/5.0',
    'Accept': 'application/json',
    'Connection': 'keep-alive',
    
    }
    response= requests.get("https://apis.digital.gob.cl/fl/feriados/2024",headers=headers,timeout=30)
    
    if response.status_code==200:
        print("API alcanzada correctamente")
        feriados= response.json()
        for feriado in feriados:
            nombre= feriado.get("nombre")
            fecha= parse_date(feriado.get("fecha"))
            tipo="nacional" if feriado["tipo"]=="Civil" else "regional"
            Feriado.objects.update_or_create(fecha=fecha,defaults={"nombre":nombre,"tipo":tipo})
        print("Feriado agregado/actualizado correctamente en la BD")
    else:
        print(f"Error en la conexion {response.status_code}")
    print("Actualizacion de los feriados finalizada correctamente")



def obtener_fecha(obj):
    if hasattr(obj,"fecha_inicio"):
        return obj.fecha_inicio
    return obj.fecha

def Calendario(request):
    obtener_feriados()
    eventos= Evento.objects.filter(estado="oficial").order_by("fecha_inicio")
    feriados= Feriado.objects.all().order_by("fecha")

    calendario= list(eventos)+list(feriados)
    calendario.sort(key=obtener_fecha)

    return render(request,"Calendario/calendario.html",{"calendario":calendario})


@login_required
def crear_evento(request):
    if request.user.rol != "administrador":
        return redirect("registration/login")
    
    if request.method == "POST":
        form= EventoForm(request.POST)
        if form.is_valid():
            form.save()
            print("Evento creado correctamente")
            return redirect("Calendario_academico")
    else:
        form= EventoForm()
    
    return render(request,"Calendario/crear_evento.html", {"form":form})

def iniciar_sesion(request):
    titulo='Inicio sesion | Tienda Verde'
    if request.method=="POST":
        usrname= request.POST['username']
        passwrd= request.POST['password']
        usuario= authenticate(request,username=usrname,password=passwrd)
        if usuario is not None:
            if usuario.rol != "administrador":
                messages.error(request,"Esta cuenta no es de un administrador")
                return redirect("Calendario_academici")
            login(request,usuario)
            return redirect('Calendario_academico')
        else:
            messages.error(request, 'Inicio de sesión incorrecto, intenta de nuevo.')

    data={
        'titulo':titulo
    }
    return render(request,'registration/login.html',data)

def cerrar_sesion(request):
    logout(request)
    return redirect('Calendario_academico')