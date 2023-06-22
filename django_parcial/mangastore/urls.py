from django.urls import path
from .views import home, colecciones, quisomos, contacto, carr, registro_usuario

urlpatterns = [
    path('', home, name='home'),    
    path('colecciones/', colecciones, name='colecciones'),    
    path('quiensomos/', quisomos, name='quiensomos'),    
    path('contacto/', contacto, name='contacto'),    
    path('carrito/', carr, name='carrito'),    
    path('registro/', registro_usuario, name='registro_usuario'),    
]