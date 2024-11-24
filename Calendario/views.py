from django.shortcuts import render,redirect
from .models import  Evento,Feriado
from .forms import EventoForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def obtener_fecha(obj):
    if hasattr(obj,"fecha_inicio"):
        return obj.fecha_inicio
    return obj.fecha

def Calendario(request):
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
            return redirect("calendario")
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
            login(request,usuario)
            return redirect('Pagina_inicio')
        else:
            messages.error(request, 'Inicio de sesión incorrecto, intenta de nuevo.')

    data={
        'titulo':titulo
    }
    return render(request,'registration/login.html',data)