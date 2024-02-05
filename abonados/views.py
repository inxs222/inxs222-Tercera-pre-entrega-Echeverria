from django.shortcuts import render
from django.db.models import Sum, Count
from .models import *
from django.http import HttpResponse
from .forms import *

def home(request):          
            debeFacturas = Facturas.objects.filter(nAbonado='14071', pago='False').count()
            totalDeuda = Facturas.objects.filter(nAbonado='14071', pago='False').aggregate(total=Sum('monto'))
            minDeuda = Facturas.objects.filter(nAbonado='14071', pago='False').aggregate(total=Sum('monto')*0.70)
            totalCobrado = Facturas.objects.filter(nAbonado='14071', pago=True ).aggregate(total=Sum('monto'))
            alertasStatus = True
            context = {'abonados': Abonado.objects.all(), 'debeFacturas': debeFacturas, 'totalDeuda': totalDeuda['total'], 'minDeuda': minDeuda['total'],
                'alertasStatus': alertasStatus, 'totalCobrado': totalCobrado['total']} 
    
            return render(request, "abonados/home.html", context)

# Servicios 
def servicios(request):
    alertasStatus = True
    nAbonado = 14071 
    context = {'servicios': Servicios.objects.all(), 'alertasStatus': alertasStatus, 'nAbonado': nAbonado} 
    return render(request, "abonados/servicios.html", context)

def serviciosForm(request):
    if request.method == "POST":
        miForm = AltaServicio(request.POST)
        if miForm.is_valid():
            s_nAbonado = miForm.cleaned_data.get("nAbonado")
            s_servicio = miForm.cleaned_data.get("servicio")
            s_servicioMonto = miForm.cleaned_data.get("servicioMonto")                                       
            servicio = Servicios(nAbonado=s_nAbonado, servicio=s_servicio, servicioMonto=s_servicioMonto)
            servicio.save()
            return render(request, "abonados/home.html")

    else:    
        miForm = AltaServicio()

    return render(request, "abonados/altaServicio.html", {"form": miForm })


def buscarServ(request):
    alertasStatus = True
    contexto = {'alertasStatus': alertasStatus}
    return render(request, "abonados/buscarServ.html", contexto)


def buscarServicios(request):
    if request.GET["buscar"]:
        alertasStatus = True
        idServicio = request.GET["buscar"]
        servicios = Servicios.objects.filter(servicio__icontains=idServicio)
        mensaje = "Se realizo  correctamente la busqueda de servicios."
        contexto = {'servicios': servicios, 'mensaje': mensaje, 'alertasStatus': alertasStatus}
        return render(request, "abonados/servicios.html", contexto)
    else:
        alertasStatus = True
        mensajeError = "No se ingreso servicio a buscar."
        contexto = {"mensaje": mensajeError, 'alertasStatus': alertasStatus}
        return render(request, "abonados/servicios.html", contexto)
    
    
# Facturas 
def facturas(request):
    alertasStatus = True
    context = {'facturas': Facturas.objects.all(), 'alertasStatus': alertasStatus} 
    return render(request, "abonados/facturas.html", context)


def facturasPagas(request):
    alertasStatus = True
    context = {'facturas': Facturas.objects.all(), 'alertasStatus': alertasStatus} 
    return render(request, "abonados/facturaspagas.html", context)

def buscarFact(request):
    alertasStatus = True
    contexto = {'alertasStatus': alertasStatus}
    return render(request, "abonados/buscarFact.html", contexto)

def buscarFacturas(request):
    if request.GET["buscar"]:
        alertasStatus = True
        factPeriodo = request.GET["buscar"]
        date = Facturas.objects.filter(date__icontains=factPeriodo)
        mensaje = "Se realizo  correctamente la busqueda de Facturas."
        contexto = {'facturas': date, 'mensaje': mensaje, 'alertasStatus': alertasStatus,
                    }
        return render(request, "abonados/facturas.html", contexto)
    else:
        alertasStatus = True
        mensajeError = "No se ingreso prediodo a buscar."
        contexto = {"mensaje": mensajeError, 'alertasStatus': alertasStatus}
        return render(request, "abonados/facturas.html", contexto)
    
def facturasForm(request):
    if request.method == "POST":
        miForm = AltaFacturas(request.POST)
        if miForm.is_valid():
            f_nAbonado = miForm.cleaned_data.get("nAbonado")
            f_nFactura = miForm.cleaned_data.get("nFactura")
            f_monto = miForm.cleaned_data.get("monto")
            f_date = miForm.cleaned_data.get("date")
            f_servicio = miForm.cleaned_data.get("servicio")
            f_pago = miForm.cleaned_data.get("pago")                                                   
            abonados = Facturas(nAbonado=f_nAbonado, nFactura=f_nFactura, monto=f_monto,
                        date=f_date, servicio=f_servicio, pago=f_pago)
            abonados.save()
            return render(request, "abonados/home.html")

    else:    
        miForm = AltaFacturas()

    return render(request, "abonados/altaFacturas.html", {"form": miForm })    

# Abonados

def listAbonados(request):
    alertasStatus = True
    context = {'abonados': Abonado.objects.all(), 'alertasStatus': alertasStatus} 
    return render(request, "abonados/listAbonados.html", context)    
    
def abonadosForm(request):
    if request.method == "POST":
        miForm = AltaAbonados(request.POST)
        if miForm.is_valid():
            ab_apellido = miForm.cleaned_data.get("apellido")
            ab_nombre = miForm.cleaned_data.get("nombre")
            ab_direccion = miForm.cleaned_data.get("direccion")
            ab_email = miForm.cleaned_data.get("email")
            ab_nAbonado = miForm.cleaned_data.get("nAbonado")                                                
            abonados = Abonado(apellido=ab_apellido, nombre=ab_nombre, direccion=ab_direccion,
                        email=ab_email, nAbonado=ab_nAbonado)
            abonados.save()
            return render(request, "abonados/home.html")

    else:    
        miForm = AltaAbonados()

    return render(request, "abonados/altaAbonados.html", {"form": miForm })

def buscarAb(request):
    alertasStatus = True
    contexto = {'alertasStatus': alertasStatus}
    return render(request, "abonados/buscarAbonados.html", contexto)

def buscarAbonados(request):
    if request.GET["buscar"]:
        alertasStatus = True
        idApellido = request.GET["buscar"]
        abonados = Abonado.objects.filter(apellido__icontains=idApellido)
        mensaje = "Se realizo  correctamente la busqueda de abonados."
        contexto = {'abonados': abonados, 'mensaje': mensaje, 'alertasStatus': alertasStatus}
        return render(request, "abonados/listAbonados.html", contexto)
    else:
        alertasStatus = True
        mensajeError = "No se ingreso servicio a buscar."
        contexto = {"mensaje": mensajeError, 'alertasStatus': alertasStatus}
        return render(request, "abonados/listAbonados.html", contexto)
    



