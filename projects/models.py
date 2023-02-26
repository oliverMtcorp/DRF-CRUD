from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre_producto = models.CharField(max_length=100)
    descripcion_producto = models.TextField()
    precio_producto = models.DecimalField(max_digits=6, decimal_places=2)
    cantidad_stock = models.IntegerField()

    def __str__(self):
        return self.nombre_producto
