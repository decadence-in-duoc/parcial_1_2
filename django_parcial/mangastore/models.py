from typing import Any
from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    activo = models.BooleanField(default=True) 
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100,)
    categoria = models.ForeignKey(Categoria, on_delete=CASCADE)
    descripcion = models.TextField(max_length=1000)
    precio = models.IntegerField()
    image = models.ImageField(upload_to='mangas', null=True, default='Some')
    available = models.BooleanField(default=True)
    def __str__(self):
        return self.nombre    
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=100)
    email = models.EmailField()
    contraseña = models.CharField(max_length=20)
    def save(self, *args, **kwargs):
        # Cifra la contraseña antes de guardarla
        self.contraseña = make_password(self.contraseña)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.nombre
    
class Factura(models.Model):
    total = models.IntegerField()
    fecha = models.DateField()
    cliente = models.ForeignKey(User, on_delete=CASCADE, null=True, blank=True)
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
    cliente = models.ForeignKey(User, on_delete=CASCADE, null=True, blank=True)
    producto = models.ForeignKey(Producto, on_delete=CASCADE)
    def __str__(self):
        return str(self.id)
    

