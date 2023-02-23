from rest_framework import serializers
from .models import Producto

class Productoserializers(serializers.ModelSerializer):
    class Meta:
        model=Producto
        fields=('nombre_producto', 'descripcion_producto', 'precio_producto', 'cantidad_stock')
        