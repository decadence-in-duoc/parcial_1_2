from django.urls import path
from .views import home, colecciones, quisomos, contacto, carr, registro_usuario, product_list, add_product, \
    mod_product, del_prod

urlpatterns = [
    path('', home, name='home'),    
    path('colecciones/', colecciones, name='colecciones'),    
    path('quiensomos/', quisomos, name='quiensomos'),    
    path('contacto/', contacto, name='contacto'),    
    path('carrito/', carr, name='carrito'),    
    path('registro/', registro_usuario, name='registro_usuario'),
    path('listaproductos/', product_list, name='product_list'),
    path('agregarproductos/', add_product, name='product_add'),
    path('modificar-producto/<id>/', mod_product, name='product_mod'),
    path('eliminar-producto/<id>/', del_prod, name='product_del'),
]