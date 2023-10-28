import strawberry
from .models import Carrito

@strawberry.django.type(Carrito)
class CarritoType:
    usuario: str
    producto: str
    cantidad: int
    estado_compra: str