from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
Roles_user=[
    ("admin","Administrador Academico"),
    ("docente","Docente"),
    ("estudiante","Estudiante")
]

Tipos_evento=[
    ("inicio_semestre","Inicio del semestre"),
    ("fin_semestre","Fin del semestre"),
    ("inicio_inscripcion","Inicio inscripcion asignaturas"),
    ("fin_inscripcion","Fin inscripcion asignaturas"),
    ("receso","Receso academico"),
    ("inicio_plazo_solicitudes","Inicio plazo solicitudes administrativas"),
    ("fin_plazo_solicitudes","Fin plazo solicitudes administrativas"),
    ("inicio_gestion_beneficios","Inicio plazo gestion de beneficios"),
    ("fin_gestion_beneficios","Fin plazo gestion de beneficios"),
    ("ceremonia_titulacion","Ceremonia de titulacion/graduacion"),
    ("reunion_consejo","Reunion consejo academico"),
    ("taller_charla","Talleres y charlas"),
    ("dia_orientacion","Dia de orientacion para alumnos nuevos"),
    ("extracurrillar","Eventos extracurriculares"),
    ("inicio_clases","Inicio de clases"),
    ("fin_clases","Ultimo dia de clases"),
    ("puertas_abiertas","Dia de puertas abiertas"),
    ("suspension_completa","Suspension completa de actividaes"),
    ("suspension_parcial","Suspension parcial de actividaes"), 
]

Tipos_feriado=[
    ("nacional","Nacional"),
    ("regional","Regional")
]

Estados_evento=[
    ("oficial","Oficial"),
    ("pendiente","Pendiente de revision"),
    ("rechazado","Rechazado"),
]



class Usuario(AbstractUser):
    rol=models.CharField(choices=Roles_user,default="estudiante")
    def __str__(self):
        return f"{self.username} es un ({self.get_rol_display()})"

class Evento(models.Model):
    titulo=models.CharField(max_length=50)
    descripcion=models.TextField(max_length=100)
    fecha_inicio=models.DateField()
    fecha_fin=models.DateField()
    tipo_evento=models.CharField(choices=Tipos_evento)
    estado=models.CharField(choices=Estados_evento,default="pendiente")

    def __str__(self):
        return f"{self.titulo} inicia el {self.fecha_inicio} terminando el {self.fecha_fin}"

class Feriado(models.Model):
    nombre=models.CharField(max_length=50)
    fecha=models.DateField(unique=True)
    tipo=models.CharField(choices=Tipos_feriado,max_length=25)

    def __str__(self):
        return f"{self.nombre} tipo {self.tipo} el {self.fecha}"

