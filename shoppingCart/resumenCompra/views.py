from django.shortcuts import render
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from resumenCompra.models import Carrito
from rest_framework.decorators import permission_classes

# Create your views here.

class ResumenCarrito(APIView):
    permission_classes = (permissions.AllowAny)

    def get(self, request, format=None):
        queryset = Carrito.objects.all()
        serializer =
