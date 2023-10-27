import strawberry
from .models import Carrito

@strawberry.django.type(Carrito)
class CarritoType:
    id: strawberry.ID
    usuario: str
    producto: str
    cantidad: int
    estado_compra: str