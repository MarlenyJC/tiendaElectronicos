from django.shortcuts import render
from django.template import RequestContext as ctx
from django.forms.models import inlineformset_factory
from django.forms import formset_factory
from django.http import HttpResponse
from django.views import View


from .models import Pedido, Detalle, Proveedor, Cliente, Almacen, Sucursal, EmpresaAsociada,Articulo
from .forms import PedidoForm,DetalleForm,ProveedorForm,ClienteForm,AlmacenForm,SucursalForm,EmpresaAsociadaForm,ArticuloForm

#from  django.contrib.auth.models import User,Group
from rest_framework import viewsets
from .serializers import AlmacenSerializer,SucursalSerializer,EmpresaAsociadaSerializer,ProveedorSerializer
from .serializers import ArticuloSerializer,ClienteSerializer,PedidoSerializer

# class UserViewSet(viewsets.ModelViewSet):
#     '' 'Ver, editar interfaz de usuario' ''
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer

class AlmacenViewSet(viewsets.ModelViewSet):
    '' 'Ver, editar interfaz de almacen' ''
    queryset = Almacen.objects.all()
    serializer_class = AlmacenSerializer

class SucursalViewSet(viewsets.ModelViewSet):
    '' 'Ver, editar interfaz de sucursal' ''
    queryset = Sucursal.objects.all()
    serializer_class = SucursalSerializer

class EmpresaAsociadaViewSet(viewsets.ModelViewSet):
    '' 'Ver, editar interfaz de empresa asociada' ''
    queryset = EmpresaAsociada.objects.all()
    serializer_class = EmpresaAsociadaSerializer

class ProveedorViewSet(viewsets.ModelViewSet):
    '' 'Ver, editar interfaz de almacen' ''
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

class ArticuloViewSet(viewsets.ModelViewSet):
    '' 'Ver, editar interfaz de articulo' ''
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    '' 'Ver, editar interfaz de cliente' ''
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    '' 'Ver, editar interfaz de pedido' ''
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer



# class GroupViewSet(viewsets.ModelViewSet):
#     '' 'Ver, editar interfaz de grupo' ''
#     queryset = Group
#     serializer_class = GroupSerializer

def home(request):
	from datetime import date
	contexto = {
					'fecha':  date.today(),
					'articulosRegistrados' : Articulo.cantidadRegistrados(),
			        'proveedoresRegistrados' :  Proveedor.cantidadRegistrados(),
			        'clientesRegistrados' : Cliente.cantidadRegistrados(),
			        'pedidosRegistrados': Pedido.cantidadRegistrados(),
			        'almacenesRegistrados':Almacen.cantidadRegistrados(),
			        'sucursalesRegistradas':Sucursal.cantidadRegistradas(),
			        'eaRegistradas':EmpresaAsociada.cantidadRegistradas(),
			        'urgentes':Pedido.urgentesRegistrados(),
			        'centroDist':Pedido.centroDistRegistrados(),
			    }
	return render(request, 'tienda/panel_principal.html',contexto)
	#return render(request, 'tienda/home.html')

class CrearPedido(View):

	def get(self,request):
		print("------")
		form = PedidoForm()
		contexto = {'form':form}
		return render(request, 'tienda/crear_pedido.html', contexto)

	def post(self,request):
		print("++++++++")
		form = PedidoForm(request.POST)

		if form.is_valid():
			request.session['cantidad_articulos'] = form.cleaned_data['cantidad_articulos']
			return HttpResponseRedirect("detallesPedido")
		else :
			#De lo contrario lanzara el mismo formulario
			return render(request, 'tienda/crear_pedido.html', {'form': form})
	# import pdb;pdb.set_trace()
	# if request.method == "POST":
	# 	form = PedidoForm(request.POST)

	# 	if form.is_valid():
	# 		request.session['cantidad_articulos'] = form.cleaned_data['cantidad_articulos']
	# 		return HttpResponseRedirect("detallesPedido")
	# 	else :
	# 		#De lo contrario lanzara el mismo formulario
	# 		return render(request, 'tienda/crear_pedido.html', {'form': form})
	# else:
	# 	form = PedidoForm()
	# 	contexto = {'form':form}
	# 	return render(request, 'tienda/crear_pedido.html', contexto)

def crear_detalles_pedido(request):
	cantidad_articulos = request.session.get('cantidad_articulos')
	if request.method == "POST":
		form = PedidoForm(request.POST)
		if form.is_valid():
			
			return HttpResponseRedirect("detallesPedido")
		else :
			#De lo contrario lanzara el mismo formulario
			return render(request, 'tienda/crear_pedido.html', {'form': form})
	else:
		PedidoFormulario = formset_factory(DetalleForm, extra=cantidad_articulos)
		formset = PedidoForm()
		contexto = {'formset':formset}
		return render(request, 'tienda/detallesPedido.html', contexto)

def eliminar_pedido(request,codigo):
	pedido = Pedido.objects.get(num_pedido=codigo)
	pedido.delete()  
	todos_pedidos = Pedido.objects.all()
	contexto = {'pedidos': todos_pedidos,}
	#import pdb;pdb.set_trace()
	return render(request, 'tienda/lista_pedidos.html', contexto)


def pedidos_filtrados(request):
	pedidos = Pedido.objects.filter(urgente=True,tipo_pedido='1',cliente_fk__tipo_cliente='platino')
	contexto = {'pedidos': pedidos,}
	#import pdb;pdb.set_trace()
	return render(request, 'tienda/lista_pedidos.html', contexto)

def pedidos(request):
	todos_pedidos = Pedido.objects.all()
	contexto = {'pedidos': todos_pedidos,}
	#import pdb;pdb.set_trace()
	return render(request, 'tienda/lista_pedidos.html', contexto)

## PROVEEDORES
def crear_proveedor(request):
	if request.method == "POST":  
		form = ProveedorForm(request.POST)  
		if form.is_valid():  
			try:  
				form.save()
				todos_proveedores = Proveedor.objects.all()
				return render(request,'tienda/lista_proveedores.html',{'proveedores': todos_proveedores,})
			except:  
				pass 
	else:  
		form = ProveedorForm()  
    
	return render(request, 'tienda/crear_proveedor.html', {'form':form})

def editar_proveedor(request, codigo):  
    proveedor = Proveedor.objects.get(codigo=codigo)
    return render(request,'tienda/editar_proveedor.html', {'proveedor':proveedor})

def actualizar_proveedor(request,codigo):
	proveedor = Proveedor.objects.get(codigo=codigo)
	form = ProveedorForm(request.POST, instance = proveedor)
	if form.is_valid():
		form.save()
		todos_proveedores = Proveedor.objects.all()
		return render(request,'tienda/lista_proveedores.html',{'proveedores': todos_proveedores,})
	return render(request, 'tienda/editar_proveedor.html', {'proveedor': proveedor})

def eliminar_proveedor(request,codigo):
	proveedor = Proveedor.objects.get(codigo=codigo)
	proveedor.delete()  
	todos_proveedores = Proveedor.objects.all()
	return render(request,'tienda/lista_proveedores.html',{'proveedores': todos_proveedores,})

def proveedores(request):
	todos_proveedores = Proveedor.objects.all()
	contexto = {'proveedores': todos_proveedores,}
	return render(request, 'tienda/lista_proveedores.html', contexto)

## CLIENTES
def crear_cliente(request):
	#import pdb;pdb.set_trace()
	if request.method == "POST":  
		form = ClienteForm(request.POST,request.FILES)  
		if form.is_valid():  
			try:  
				form.save()
				todos_clientes = Cliente.objects.all()
				return render(request,'tienda/lista_clientes.html',{'clientes': todos_clientes,})
			except:  
				pass
		else :
			return HttpResponse("Form is invalid!")
	else:  
		form = ClienteForm()  
    
	return render(request, 'tienda/crear_cliente.html', {'form':form})

def editar_cliente(request, codigo):
    print("---")
    cliente = Cliente.objects.get(codigo=codigo)
    return render(request,'tienda/editar_cliente.html', {'cliente':cliente})

def actualizar_cliente(request,codigo):
	cliente = Cliente.objects.get(codigo=codigo)
	form = ClienteForm(request.POST, instance = cliente)
	if form.is_valid():
		form.save()
		todos_clientes = Cliente.objects.all()
		return render(request,'tienda/lista_clientes.html',{'clientes': todos_clientes,})
	return render(request, 'tienda/editar_cliente.html', {'cliente': cliente})

def eliminar_cliente(request,codigo):
	cliente = Cliente.objects.get(codigo=codigo)
	cliente.delete()  
	todos_clientes = Cliente.objects.all()
	return render(request,'tienda/lista_clientes.html',{'clientes': todos_clientes,})

def clientes(request):
	todos_clientes = Cliente.objects.all()
	contexto = {'clientes': todos_clientes,}
	return render(request, 'tienda/lista_clientes.html', contexto)


## ALMACENES
def crear_almacen(request):
	if request.method == "POST":  
		form = AlmacenForm(request.POST)  
		if form.is_valid():  
			try:  
				form.save()
				todos_almacenes = Almacen.objects.all()
				return render(request,'tienda/lista_almacenes.html',{'almacenes': todos_almacenes,})
			except:  
				pass 
	else:  
		form = AlmacenForm()  
    
	return render(request, 'tienda/crear_almacen.html', {'form':form})

def editar_almacen(request, codigo):  
    almacen = Almacen.objects.get(codigo=codigo)
    return render(request,'tienda/editar_almacen.html', {'almacen':almacen})

def actualizar_almacen(request,codigo):
	almacen = Almacen.objects.get(codigo=codigo)
	form = AlmacenForm(request.POST, instance = almacen)
	if form.is_valid():
		form.save()
		todos_almacenes = Almacen.objects.all()
		return render(request,'tienda/lista_almacenes.html',{'almacenes': todos_almacenes,})
	return render(request, 'tienda/editar_almacen.html', {'almacen': almacen})

def eliminar_almacen(request,codigo):
	almacen = Almacen.objects.get(codigo=codigo)
	almacen.delete()  
	todos_almacenes = Almacen.objects.all()
	return render(request,'tienda/lista_almacenes.html',{'almacenes': todos_almacenes,})

def almacenes(request):
	todos_almacenes = Almacen.objects.all()
	contexto = {'almacenes': todos_almacenes,}
	return render(request, 'tienda/lista_almacenes.html', contexto)

## SUCURSALES
def crear_sucursal(request):
	if request.method == "POST":  
		form = SucursalForm(request.POST)  
		if form.is_valid():  
			try:  
				form.save()
				todos_sucursales = Sucursal.objects.all()
				return render(request,'tienda/lista_sucursales.html',{'sucursales': todos_sucursales,})
			except:  
				pass 
	else:  
		form = SucursalForm()  
    
	return render(request, 'tienda/crear_sucursal.html', {'form':form})

def editar_sucursal(request, codigo):  
    sucursal = Sucursal.objects.get(codigo=codigo)
    return render(request,'tienda/editar_sucursal.html', {'sucursal':sucursal})

def actualizar_sucursal(request,codigo):
	sucursal = Sucursal.objects.get(codigo=codigo)
	form = SucursalForm(request.POST, instance = sucursal)
	if form.is_valid():
		form.save()
		todos_sucursales = Sucursal.objects.all()
		return render(request,'tienda/lista_sucursales.html',{'sucursales': todos_sucursales,})
	return render(request, 'tienda/editar_sucursal.html', {'sucursal': sucursal})

def eliminar_sucursal(request,codigo):
	sucursal = Sucursal.objects.get(codigo=codigo)
	sucursal.delete()  
	todos_sucursales = Sucursal.objects.all()
	return render(request,'tienda/lista_sucursales.html',{'sucursales': todos_sucursales,})

def sucursales(request):
	todos_sucursales = Sucursal.objects.all()
	contexto = {'sucursales': todos_sucursales,}
	return render(request, 'tienda/lista_sucursales.html', contexto)

## EMPRESAS ASOCIADAS
def crear_empresa_asociada(request):
	if request.method == "POST":  
		form = EmpresaAsociadaForm(request.POST)  
		if form.is_valid():  
			try:  
				form.save()
				todos_ea = EmpresaAsociada.objects.all()
				return render(request,'tienda/lista_empresas_asociadas.html',{'empresas_asociadas': todos_ea,})
			except:  
				pass 
	else:  
		form = EmpresaAsociadaForm()  
    
	return render(request, 'tienda/crear_empresa_asociada.html', {'form':form})

def editar_empresa_asociada(request, codigo):  
    empresa_asociada = EmpresaAsociada.objects.get(codigo=codigo)
    return render(request,'tienda/editar_empresa_asociada.html', {'empresa_asociada':empresa_asociada})

def actualizar_empresa_asociada(request,codigo):
	empresa_asociada = EmpresaAsociada.objects.get(codigo=codigo)
	form = EmpresaAsociadaForm(request.POST, instance = empresa_asociada)
	if form.is_valid():
		form.save()
		todos_ea = EmpresaAsociada.objects.all()
		return render(request,'tienda/lista_empresas_asociadas.html',{'empresas_asociadas': todos_ea,})
	return render(request, 'tienda/editar_empresa_asociada.html', {'empresa_asociada': empresa_asociada})

def eliminar_empresa_asociada(request,codigo):
	empresa_asociada = EmpresaAsociada.objects.get(codigo=codigo)
	empresa_asociada.delete()  
	todos_ea = EmpresaAsociada.objects.all()
	return render(request,'tienda/lista_empresas_asociadas.html',{'empresas_asociadas': todos_ea,})

def empresas_asociadas(request):
	todos_ea = EmpresaAsociada.objects.all()
	contexto = {'empresas_asociadas': todos_ea,}
	return render(request, 'tienda/lista_empresas_asociadas.html', contexto)

## ARTÍCULOS
def crear_articulo(request):
	if request.method == "POST":  
		form = ArticuloForm(request.POST)
		import pdb;pdb.set_trace()  
		if form.is_valid():  
			try:  
				form.save()
				todos_articulos = Articulo.objects.all()
				return render(request,'tienda/lista_articulos.html',{'articulos': todos_articulos,})
			except:  
				pass 
	else:  
		form = ArticuloForm()  
    
	return render(request, 'tienda/crear_articulo.html', {'form':form})

def editar_articulo(request, codigo):  
    articulo = Articulo.objects.get(codigo=codigo)
    proveedores = articulo.proveedores.all()
    return render(request,'tienda/editar_articulo.html', {'articulo':articulo, 
    													  'proveedores':proveedores})

def actualizar_articulo(request,codigo):
	articulo = Articulo.objects.get(codigo=codigo)
	form = ArticuloForm(request.POST, instance = articulo)
	import pdb;pdb.set_trace()
	if form.is_valid():
		form.save()
		todos_articulos = Articulo.objects.all()
		return render(request,'tienda/lista_articulos.html',{'articulos': todos_articulos,})
	return render(request, 'tienda/editar_articulo.html', {'articulo': articulo})

def eliminar_articulo(request,codigo):
	articulo = Articulo.objects.get(codigo=codigo)
	articulo.delete()  
	todos_articulos = Articulo.objects.all()
	return render(request,'tienda/lista_articulos.html',{'articulos': todos_articulos,})

def articulos(request):
	todos_articulos = Articulo.objects.all()
	contexto = {'articulos': todos_articulos,}
	return render(request, 'tienda/lista_articulos.html', contexto)


