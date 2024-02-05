from django.db import models

# Create your models here.
class Abonado(models.Model):
    apellido = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    email = models.EmailField()
    nAbonado = models.IntegerField()

    def __str__(self):
        return f"{self.nAbonado}, {self.apellido.upper()}, {self.nombre.upper()}"

class Facturas(models.Model):
    nAbonado = models.IntegerField()
    nFactura = models.IntegerField()
    monto = models.IntegerField()
    date = models.DateTimeField()
    servicio = models.CharField(max_length=50)
    pago = models.BooleanField()

    def __str__(self):
        return f"N_Abonado {self.nAbonado}, N_Factura {self.nFactura}, Monto {self.monto} , Fecha {self.date}"
    
    
class Servicios(models.Model):
    nAbonado = models.IntegerField()
    servicio = models.CharField(max_length=250)
    servicioMonto = models.IntegerField()
    
    def __str__(self):
        return f"N_Abonado {self.nAbonado} Servicio {self.servicio}  Monto {self.servicioMonto}"