from django.db import models
import datetime
import re


class Cliente(models.Model):
	TIPOS_CLIENTES = (
						('normal','NORMAL'),
						('plata','PLATA'),
						('oro','ORO'),
						('platino','PLATINO'),
					)
	codigo = models.CharField(max_length=5, primary_key=True)
	nombre = models.CharField(max_length=60)
	fotografia = models.ImageField(upload_to='albums/images/',null=True, blank=True)
	direccion = models.CharField(max_length=100)
	tipo_cliente = models.CharField(max_length=7, choices=TIPOS_CLIENTES, default='normal')

	def __str__(self):
		txt = "{0} {1}"
		return txt.format(self.codigo,self.nombre)

	@classmethod
	def clientesRegistrados(self):
		objetos = self.objects.all().order_by('codigo')
		return objetos

	@classmethod
	def cantidadRegistrados(self):
		return int(self.objects.all().count() )

class Proveedor(models.Model):
	codigo = models.CharField(max_length=5, primary_key=True)
	nombre = models.CharField(max_length=60)
	direccion = models.CharField(max_length=100, default='')

	def __str__(self):
		txt = "{0} {1}"
		return txt.format(self.codigo,self.nombre)

	@classmethod
	def cantidadRegistrados(self):
		return int(self.objects.all().count() )

class Almacen(models.Model):
	codigo = models.CharField(max_length=5, primary_key=True)
	nombre = models.CharField(max_length=60)
	direccion = models.CharField(max_length=100, default='')

	def __str__(self):
		txt = "{0} {1}"
		return txt.format(self.codigo,self.nombre)

	@classmethod
	def almacenesRegistrados(self):
		objetos = self.objects.all().order_by('codigo')
		return objetos

	@classmethod
	def cantidadRegistrados(self):
		return int(self.objects.all().count() )

class Sucursal(models.Model):
	codigo = models.CharField(max_length=5, primary_key=True)
	nombre = models.CharField(max_length=60)
	direccion = models.CharField(max_length=100, default='')

	def __str__(self):
		txt = "{0} {1}"
		return txt.format(self.codigo,self.nombre)

	@classmethod
	def sucursalesRegistradas(self):
		objetos = self.objects.all().order_by('codigo')
		return objetos

	@classmethod
	def cantidadRegistradas(self):
		return int(self.objects.all().count() )

	@classmethod
	def generaCodigo(self):
		ultima_suc = self.objects.last()
		er = re.compile('[0-9]{4}')

		if ultima_suc :
			ult_codigo = ultima_suc.codigo
			er_codigo = er.search(ult_codigo)
			nuevo_codigo = str(int(er_codigo.group()) + 1)
			nuevo_codigo = 'S'+nuevo_codigo.zfill(4)
		else :
			nuevo_codigo = 'S0001'

		return nuevo_codigo

class EmpresaAsociada(models.Model):
	codigo = models.CharField(max_length=5, primary_key=True)
	nombre = models.CharField(max_length=60)
	direccion = models.CharField(max_length=100, default='')

	def __str__(self):
		txt = "{0} {1}"
		return txt.format(self.codigo,self.nombre)

	@classmethod
	def eaRegistradas(self):
		objetos = self.objects.all().order_by('codigo')
		return objetos

	@classmethod
	def cantidadRegistradas(self):
		return int(self.objects.all().count() )

class Articulo(models.Model):
	codigo = models.CharField(max_length=5, primary_key=True)
	descripcion = models.CharField(max_length=50)
	monto = models.FloatField(default=0.0)
	proveedores = models.ManyToManyField(Proveedor)

	def __str__(self):
		txt = "{0} {1}"
		return txt.format(self.codigo,self.descripcion)

	@classmethod
	def articulosRegistrados(self):
		objetos = self.objects.all().order_by('codigo')
		return objetos

	@classmethod
	def cantidadRegistrados(self):
		return int(self.objects.all().count() )
	
class Pedido(models.Model):
	TIPOS_PEDIDOS = [
						('1','El Centro de Distribución'),
						('2','Alguna Sucursal'),
						('3','Una empresa asociada'),
					]
	num_pedido = models.CharField(max_length=5, primary_key=True)
	cliente_fk = models.ForeignKey(Cliente, on_delete=models.CASCADE)
	fecha_genera_pedido = models.DateField(auto_now_add=True)
	fecha_surte_pedido = models.DateField(auto_now_add=True)
	urgente = models.BooleanField(default=False)
	tipo_pedido = models.CharField(max_length=1, choices=TIPOS_PEDIDOS, default='1')
	almacen_a_surtir_fk = models.ForeignKey(Almacen, on_delete=models.CASCADE) #si tipo_pedido=1
	referencia = models.CharField(max_length=10, blank=True) #si tipo_pedido= 2 o 3
	codigo_sucursal_fk = models.ForeignKey(Sucursal, on_delete=models.CASCADE) #si tipo_pedido=2
	codigo_socio_fk = models.ForeignKey(EmpresaAsociada, on_delete=models.CASCADE) #si tipo_pedido=3
	monto_total = models.FloatField(default=0.0)
	#surtido = models.BooleanField(default=False, blank=True)

	def __str__(self):
		txt = "{0} {1}"
		return txt.format(self.num_pedido,self.cliente_fk.nombre)

	@classmethod
	def generaCodigo(self):
		ultimo_pedido = self.objects.last()
		er = re.compile('[0-9]{3}')
		#import pdb;pdb.set_trace()
		if ultimo_pedido :
			ult_num_pedido = ultimo_pedido.num_pedido
			er_num_pedido = er.search(ult_num_pedido)
			nuevo_num_pedido = str(int(er_num_pedido.group()) + 1)
			nuevo_num_pedido = 'PE'+nuevo_num_pedido.zfill(3)
		else :
			nuevo_num_pedido = 'PE001'

		return nuevo_num_pedido

	@classmethod
	def cantidadRegistrados(self):
		return int(self.objects.all().count() )

	@classmethod
	def urgentesRegistrados(self):
		return int(self.objects.filter(urgente=True).count() )

	@classmethod
	def centroDistRegistrados(self):
		return int(self.objects.filter(tipo_pedido='1').count() )

class Detalle(models.Model):
	pedido_fk = models.ForeignKey(Pedido, on_delete=models.CASCADE)
	articulo_fk = models.ForeignKey(Articulo, on_delete=models.CASCADE)
	cantidad = models.IntegerField(default=0)

	def __str__(self):
		txt = "{0} / {1} {2}"
		return txt.format(self.pedido_fk.num_pedido,self.articulo_fk.codigo,self.articulo_fk.descripcion)


# class Detalle2(models.Model):
# 	pedido_fk = models.ForeignKey(Pedido, on_delete=models.CASCADE)
# 	articulo_fk = models.ManyToManyField(Articulo)
# 	cantidad = models.IntegerField(default=0)
# 	monto_unitario = models.FloatField(default=0.0)
# 	monto_total = models.FloatField(default=0.0)	

