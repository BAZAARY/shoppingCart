from django.urls import path
from .views import ResumenCarrito

urlpatterns = [
    path("getProducts", ResumenCarrito.as_view()),
]