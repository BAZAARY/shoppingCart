import strawberry
from typing import List
from .types import CarritoType
from .models import Carrito

@strawberry.type
class Query:
    @strawberry.field
    def listuserproducts(self, usuario:int) -> List[CarritoType]:
            if usuario:
                  products = Carrito.objects.filter(usuario=usuario)
                  return products
            return Carrito.objects.all()
    
@strawberry.type
class Mutation:
      @strawberry.mutation
      def addproduct(self, usuario:int, producto:int) -> CarritoType:
            nuevoProducto = Carrito(usuario=usuario, producto=producto)
            nuevoProducto.save(force_insert=True)
            return nuevoProducto
      @strawberry.mutation
      def deleteproduct(self, usuario:int, producto:int) -> bool:
            try: 
                  Carrito.objects.filter(usuario=usuario, producto=producto).delete()
                  return True  
            except CarritoType.DoesNotExist:
                  return False  

      
schema = strawberry.federation.Schema(query=Query, mutation=Mutation)