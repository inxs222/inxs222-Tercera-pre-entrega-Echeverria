from django import forms   

class AltaAbonados(forms.Form):
    apellido = forms.CharField(max_length=50)
    nombre = forms.CharField(max_length=50)
    direccion = forms.CharField(max_length=50)
    email = forms.EmailField()
    nAbonado = forms.IntegerField()


class AltaServicio(forms.Form):
    nAbonado = forms.IntegerField()
    servicio = forms.CharField(max_length=250)
    servicioMonto = forms.IntegerField()


class AltaFacturas(forms.Form):
    nAbonado = forms.IntegerField()
    nFactura = forms.IntegerField()
    monto = forms.IntegerField()
    date = forms.DateTimeField()
    servicio = forms.CharField(max_length=50)
    pago = forms.BooleanField()