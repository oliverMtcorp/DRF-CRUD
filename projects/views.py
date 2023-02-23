from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view 
from .models import Producto
from .serializers import Productoserializers



@api_view(['GET'])
def getProducto(request):
    producto = Producto.objects.all()
    serializer = Productoserializers(producto, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getSoloProducto(request, pk):
    producto = Producto.objects.get(pk=pk)
    serializer = Productoserializers(producto, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def postProducto(request):
    serializer = Productoserializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def putProducto(request, pk):
    data = request.data
    producto = Producto.objects.get(id=pk)
    serializer = Productoserializers(instance=producto, data=data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteProducto(request, pk):
    producto = Producto.objects.get(id=pk)
    producto.delete()
    return Response('Producto Eliminado')