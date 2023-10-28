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
    
@strawberry.type
class Mutation:
      @strawberry.mutation
      def addproduct(self, usuario:str) -> CarritoType:
            nuevoProducto = Carrito(usuario=usuario)
            nuevoProducto.save()
            return nuevoProducto
      
schema = strawberry.federation.Schema(query=Query, mutation=Mutation)