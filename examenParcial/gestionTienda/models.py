
from django.db import models

class Tienda(models.Model):
    direccion = models.CharField(max_length=255)
    provincia = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    fecha_creacion = models.DateField()
    telefono_contacto = models.CharField(max_length=20)

    def __str__(self):
        return f'Tienda: {self.direccion} ({self.region})'

class Producto(models.Model):
    descripcion = models.CharField(max_length=255)
    codigo = models.CharField(max_length=50, unique=True)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.PositiveIntegerField()
    tienda_relacionada = models.ForeignKey(Tienda, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'Producto: {self.descripcion} ({self.codigo})'