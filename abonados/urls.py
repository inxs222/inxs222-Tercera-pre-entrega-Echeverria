from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('facturas/', facturas, name="facturas"),
    path('facturaspagas/', facturasPagas, name="facturasPagas"),
    path('servicios/', servicios, name="servicios"),

    path('buscarServ/', buscarServ, name="buscarServ"),
    path('buscarServicios/', buscarServicios, name="buscarServicios"),
    path('altaServicio', serviciosForm, name="altaServicio"),
    
    path('buscarFact/', buscarFact, name="buscarFact"),
    path('buscarFacturas/', buscarFacturas, name="buscarFacturas"),
    path('altaFacturas/', facturasForm, name="altaFacturas"),
    
    path('altaAbonados/', abonadosForm, name="altaAbonados"),
    path('listAbonados/', listAbonados, name="listAbonados"),
    path('buscarAbonados/', buscarAbonados, name="buscarAbonados"),
    path('buscarAb/', buscarAb, name="buscarAb"),    
]