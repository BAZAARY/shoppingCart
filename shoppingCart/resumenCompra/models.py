# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Carrito(models.Model):
    usuario = models.CharField(max_length=255, primary_key=True)
    producto = models.CharField(max_length=255, unique=True, default="")
    cantidad = models.SmallIntegerField(default=1)
    estado_compra = models.CharField(max_length=255, default="inmediata")
    
    class Meta:
        managed = False
        db_table = 'carrito'
        unique_together = ('usuario', 'producto'),
        db_table_comment = 'Tabla para el carrito de compras'


