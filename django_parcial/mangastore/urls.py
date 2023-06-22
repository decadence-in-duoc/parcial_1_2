from django.urls import path
from .views import add_manga, eliminar_producto, home, colecciones, lista_manga, mod_prod, quisomos, contacto, carr

urlpatterns = [
    path('', home, name='home'),    
    path('colecciones/', colecciones, name='colecciones'),    
    path('quiensomos/', quisomos, name='quiensomos'),    
    path('contacto/', contacto, name='contacto'),    
    path('carrito/', carr, name='carrito'),
    path('lista_manga/', lista_manga, name='lista_manga'),
    path('add_manga/', add_manga, name='add_manga'),  
    path('mod_prod/', mod_prod, name='mod_prod'),
    path('eliminar_producto/', eliminar_producto, name='eliminar_producto'),    
]