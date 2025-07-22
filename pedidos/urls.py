from django.urls import path
from . import views

urlpatterns = [
    # Ruta para la página principal (Home)
    path('', views.home, name='home'),

    # Rutas para gestionar Clientes
    path('clientes/', views.gestionar_clientes, name='gestionar_clientes'),
    
    # Rutas para gestionar Proveedores
    path('proveedores/', views.gestionar_proveedores, name='gestionar_proveedores'),
    
    # Rutas para gestionar Categorías
    path('categorias/', views.gestionar_categorias, name='gestionar_categorias'),
    
    # Rutas para gestionar Productos
    path('productos/', views.gestionar_productos, name='gestionar_productos'),
    
    # Rutas para gestionar Pedidos
    path('pedidos/', views.gestionar_pedidos, name='gestionar_pedidos'),
    
    # Rutas para gestionar Detalles de Pedido
    path('detalles_pedido/', views.gestionar_detalle_pedidos, name='gestionar_detalle_pedidos'),
]
