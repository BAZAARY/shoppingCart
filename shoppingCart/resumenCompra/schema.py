import strawberry
from typing import List
from .types import CarritoType
from .models import Carrito

@strawberry.type
class Query:
    @strawberry.field
    def products(self, usuario:str = None) -> List[CarritoType]:
            if usuario:
                  products = Carrito.objects.filter(usuario=usuario)
                  return products
            return Carrito.objects.all()
    

schema = strawberry.federation.Schema(query=Query)