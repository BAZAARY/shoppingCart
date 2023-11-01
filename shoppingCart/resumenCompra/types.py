import strawberry
from .models import Carrito

@strawberry.django.type(Carrito)
class CarritoType:
    usuario: int
    producto: int
    cantidad: int
    estado_compra: str