from django.contrib import admin
from .models import Categoria, Producto, Factura, Carrito, Cliente, DetalleProducto
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'categoria', 'descripcion', 'precio']
    
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'telefono', 'direccion', 'email']
    
class FacturaAdmin(admin.ModelAdmin):
    list_display = ['id','total', 'fecha', 'cliente']
    
class CarritoAdmin(admin.ModelAdmin):
    list_display = ['id','cantidad', 'cliente', 'producto']
    
class DetalleAdmin(admin.ModelAdmin):
    list_display = ['id','cantidad', 'subtotal', 'producto', 'factura']


admin.site.register(Categoria),
admin.site.register(Producto, ProductoAdmin),
admin.site.register(Factura, FacturaAdmin),
admin.site.register(Carrito, CarritoAdmin),
admin.site.register(Cliente, ClienteAdmin),
admin.site.register(DetalleProducto, DetalleAdmin),

