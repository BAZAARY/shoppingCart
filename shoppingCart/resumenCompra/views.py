from django.shortcuts import render
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from resumenCompra.models import Carrito
from rest_framework.decorators import permission_classes
from resumenCompra.serializers import CarritoSerializer
# Create your views here.

class ResumenCarrito(APIView):
    #Retorna todos los elementos del carrito
    #Este metodo se actualizará eventualmente cuando pueda recuperar el token de auth
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        queryset = Carrito.objects.all()
        serializer = CarritoSerializer(queryset, many=True)
        return Response(serializer.data)