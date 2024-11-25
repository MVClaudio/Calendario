from rest_framework import routers
from django.urls import path, include
from .views import EventoViewSet,FeriadoViewSet,CalendarioViewSet

router = routers.DefaultRouter()
router.register(r'evento',EventoViewSet)
router.register(r"feriados",FeriadoViewSet)

urlpatterns=[
    path("",include(router.urls)),
    path("calendario/",CalendarioViewSet.as_view(),name="Calendario completo")
]