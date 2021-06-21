# Serialización
from  rest_framework import serializers
from .models import Pedido, Detalle, Proveedor, Cliente, Almacen, Sucursal, EmpresaAsociada,Articulo

class AlmacenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
    	model = Almacen
    	fields = "__all__"

class SucursalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
    	model = Sucursal
    	fields = "__all__"

class EmpresaAsociadaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
    	model = EmpresaAsociada
    	fields = "__all__"

class ProveedorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
    	model = Proveedor
    	fields = "__all__"

class ArticuloSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
    	model = Articulo
    	fields = "__all__"

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
    	model = Cliente
    	fields = "__all__"

class PedidoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
    	model = Pedido
    	fields = "__all__"
