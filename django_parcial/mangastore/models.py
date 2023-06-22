from typing import Any
from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    activo = models.BooleanField(default=True) 
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100,)
    categoria = models.ForeignKey(Categoria, on_delete=CASCADE)
    descripcion = models.CharField(max_length=200)
    precio = models.IntegerField()
    def __str__(self):
        return self.nombre    
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=100)
    email = models.EmailField()
    contraseña = models.CharField(max_length=20)
    def __str__(self):
        return self.nombre
    
class Factura(models.Model):
    total = models.IntegerField()
    fecha = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=CASCADE)
    def __str__(self):
        return str(self.id)
        
class DetalleProducto(models.Model):
    cantidad = models.IntegerField()
    subtotal = models.IntegerField()
    producto = models.ForeignKey(Producto, on_delete=CASCADE)
    factura = models.ForeignKey(Factura, on_delete=CASCADE)
    def __str__(self):
        return str(self.id)
    
class Carrito(models.Model):
    cantidad = models.IntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=CASCADE)
    producto = models.ForeignKey(Producto, on_delete=CASCADE)
    def __str__(self):
        return str(self.id)

