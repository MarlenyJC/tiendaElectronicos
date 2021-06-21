# Tienda de electrónicos
Sistema de pedidos hecho con Django

El sistema permite realizar operaciones básicas de registro, edición y eliminación:

-Cuenta con los siguientes modelos y funcionalidades: 
	-Cliente: Visualizar todos - Agregar - Editar - Eliminar
	-Proveedor: Visualizar todos - Agregar - Editar - Eliminar
	-Almacen: Visualizar todos - Agregar - Editar - Eliminar
	-Sucursal: Visualizar todas - Agregar - Editar - Eliminar
	-Empresa Asociada: Visualizar todas - Agregar - Editar - Eliminar
	-Artículo: Visualizar todos - Agregar - Eliminar
	-Pedido: Visualizar todos - Eliminar - Obtener un filtro específico de los pedidos (Pedidos Urgentes a centros de distribución que pertenecen a cliente PLATINO y que no se han surtido)

#URL de cada modelo
-Inicio: http://127.0.0.1:8000/
-Cliente: http://127.0.0.1:8000/clientes/
-Proveedor: http://127.0.0.1:8000/proveedores/
-Almacen: http://127.0.0.1:8000/almacenes/
-Sucursal: http://127.0.0.1:8000/sucursales/
-Empresa Asociada: http://127.0.0.1:8000/empresas_asociadas/
-Artículo: http://127.0.0.1:8000/articulos/
-Pedido: http://127.0.0.1:8000/pedidos/

# Limitaciones básicas:
-No agrega pedidos *
-No agrega detalles de pedido *
-No es posible visualizar la fotografía capturada en el Cliente

*Para efectos de prueba los datos de pedidos fueron agregados desde el administrador de Django


#Documentación de los modelos del sistema
url : http://127.0.0.1:8000/docs/


#Ejecución del sistema
-Entrar al directorio 
cd /tiendaElectronicos
python manage.py runserver


#Administrador de Django
Administrador de Django
http://127.0.0.1:8000/admin/
Username: admin
Contraseña: admin


# Dependencias:
Django==3.2.4
django-rest-swagger==2.2.0
djangorestframework==3.12.4
PyYAML==5.4.1

Después de instalar estos paquetes el entorno queda con todos los paquetes que se encuentran en el archivo requirements.txt



