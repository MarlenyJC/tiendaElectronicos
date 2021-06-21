from django.urls import path
from . import views 
#import home,crear_pedido,pedidos,crear_proveedor,proveedores,editar_proveedor,actualizar_proveedor,eliminar_proveedor

urlpatterns = [
    path('', views.home, name='home'),
    #path('panel', views.PanelPrincipal.as_view(), name='panel'),
    #Pedidos
    path('crearpedido/', views.CrearPedido.as_view(), name='crearpedido'),
    path('detallesPedido', views.crear_detalles_pedido, name='detallespedido'),
    path('eliminarpedido/<str:codigo>', views.eliminar_pedido, name='eliminarpedido'),
    path('pedidosfiltrados/', views.pedidos_filtrados, name='pedidosfiltrados'),
    path('pedidos/', views.pedidos, name='pedidos'),
    #Proveedores
    path('crearproveedor/', views.crear_proveedor, name='crearproveedor'),
    path('editarproveedor/<str:codigo>/', views.editar_proveedor, name='editarproveedor'),
    path('actualizarproveedor/<str:codigo>', views.actualizar_proveedor, name='actualizarproveedor'),
    path('eliminarproveedor/<str:codigo>', views.eliminar_proveedor, name='eliminarproveedor'),
    path('proveedores/', views.proveedores, name='proveedores'),
    #Clientes
    path('crearcliente/', views.crear_cliente, name='crearcliente'),
    path('editarcliente/<str:codigo>/', views.editar_cliente, name='editarcliente'),
    path('actualizarcliente/<str:codigo>', views.actualizar_cliente, name='actualizarcliente'),
    path('eliminarcliente/<str:codigo>', views.eliminar_cliente, name='eliminarcliente'),
    path('clientes/', views.clientes, name='clientes'),
    #Almacenes
    path('crearalmacen/', views.crear_almacen, name='crearalmacen'),
    path('editaralmacen/<str:codigo>/', views.editar_almacen, name='editaralmacen'),
    path('actualizaralmacen/<str:codigo>', views.actualizar_almacen, name='actualizaralmacen'),
    path('eliminaralmacen/<str:codigo>', views.eliminar_almacen, name='eliminaralmacen'),
    path('almacenes/', views.almacenes, name='almacenes'),
    #Sucursales
    path('crearsucursal/', views.crear_sucursal, name='crearsucursal'),
    path('editarsucursal/<str:codigo>/', views.editar_sucursal, name='editarsucursal'),
    path('actualizarsucursal/<str:codigo>', views.actualizar_sucursal, name='actualizarsucursal'),
    path('eliminarsucursal/<str:codigo>', views.eliminar_sucursal, name='eliminarsucursal'),
    path('sucursales/', views.sucursales, name='sucursales'),
    #Empresas asociadas
    path('crearempresa_asociada/', views.crear_empresa_asociada, name='crearempresa_asociada'),
    path('editarempresaasociada/<str:codigo>/', views.editar_empresa_asociada, name='editarempresaasociada'),
    path('actualizarempresaasociada/<str:codigo>', views.actualizar_empresa_asociada, name='actualizarempresaasociada'),
    path('eliminarempresa_asociada/<str:codigo>', views.eliminar_empresa_asociada, name='eliminarempresa_asociada'),
    path('empresas_asociadas/', views.empresas_asociadas, name='empresas_asociadas'),
    #Artículos
    path('creararticulo/', views.crear_articulo, name='creararticulo'),
    path('editararticulo/<str:codigo>/', views.editar_articulo, name='editararticulo'),
    path('actualizararticulo/<str:codigo>', views.actualizar_articulo, name='actualizararticulo'),
    path('eliminararticulo/<str:codigo>', views.eliminar_articulo, name='eliminararticulo'),
    path('articulos/', views.articulos, name='articulos'),

]