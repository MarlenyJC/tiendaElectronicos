#forms.py
from django import forms  
from .models import Pedido, Detalle, Proveedor, Cliente, Almacen, Sucursal, EmpresaAsociada, Articulo
from django.forms.models import inlineformset_factory
from django.forms.models import ModelMultipleChoiceField
from django.forms import ModelChoiceField


class Clientes(ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s %s" % (obj.codigo,obj.nombre)

class Almacenes(ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s %s" % (obj.codigo,obj.nombre)

class Sucursales(ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s %s" % (obj.codigo,obj.nombre)

class EmpresasAsociadas(ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s %s" % (obj.codigo,obj.nombre)


class PedidoForm(forms.Form):
    # class Meta:  
    #     model = Pedido

    # fields = ['num_pedido', 'cliente_fk','fecha_surte_pedido', #fecha_genera_pedido
    #      'urgente','tipo_pedido','almacen_a_surtir_fk','referencia','codigo_sucursal_fk',
    #      'codigo_socio_fk','monto_total']
        
        # widgets = { 'num_pedido': forms.TextInput(),
        #             'cliente_fk': forms.TextInput(),
        #             #'fecha_genera_pedido': forms.DateInput(attrs={ 'class': 'form-control','readonly':'true' }),
        #             'fecha_surte_pedido': forms.DateInput(attrs={ 'type':'date' }),
        #             'tipo_pedido': forms.TextInput(),
        #             'almacen_a_surtir_fk': forms.TextInput(),
        #             'referencia': forms.TextInput(),
        #             'codigo_sucursal_fk': forms.TextInput(),
        #             'codigo_socio_fk': forms.TextInput(),
        #             'monto_total': forms.NumberInput(),
        #         }
    clientes_registrados = Cliente.clientesRegistrados()
    TIPOS_PEDIDOS = [
                        ('1','El Centro de Distribución'),
                        ('2','Alguna Sucursal'),
                        ('3','Una empresa asociada'),
                    ]
    almacenes_registrados = Almacen.almacenesRegistrados()
    nuevo_num_pedido = Pedido.generaCodigo()
    sucursales_registradas = Sucursal.sucursalesRegistradas()
    ea_registradas = EmpresaAsociada.eaRegistradas()

    num_pedido = forms.CharField(label = 'Número de Pedido',
                                    max_length = 5,
                                    widget = forms.TextInput(attrs={'class':'form-control',
                                                                    'id':'num_pedido',
                                                                    'readonly':True,
                                                                    'value':nuevo_num_pedido}), 
                                    )
    fecha_surte_pedido = forms.DateField(label='Fecha de surtido del pedido',
                                          widget= forms.DateInput(attrs={ 'class': 'form-control'}))
    cliente = Clientes(label="Cliente",queryset=clientes_registrados,
                        widget=forms.Select(attrs={'placeholder': 'Cliente',
                                                   'class':'form-control',}))
    fecha_surte_pedido = forms.CharField(label='Fecha de surtido del pedido', required=False,
                                          widget= forms.DateInput(format=('%d-%m-%Y'),
                                                                  attrs={ 'class': 'form-control','type':'date'}))
    tipo_pedido = forms.CharField(
                                  label="Dirigido hacia",
                                  max_length=2,
                                  widget=forms.Select(choices=TIPOS_PEDIDOS,attrs={'placeholder': 'Hacia donde se realiza el pedido',
                                                      'id':'tipo_pedido',
                                                      'class':'form-control',
                                                      'value':''}
                                  )
                            )
    almacen_a_surtir_fk = Almacenes(
                                    label='Almacen',
                                    queryset=almacenes_registrados,
                                    widget=forms.Select(attrs={'placeholder': 'Almacen',
                                                               'class':'form-control',
                                                               'id':'almacen_a_surtir_fk'})
                                    )
    referencia = forms.CharField(label='Referencia',
                                 widget=forms.TextInput(attrs={'class':'form-control',
                                                                'id':'referencia',
                                                                'readonly':False,
                                                                'value':''})
                                )
    codigo_sucursal_fk = Sucursales(
                                    label='Sucursal',
                                    queryset=sucursales_registradas,
                                    widget=forms.Select(attrs={'placeholder': 'Sucursal',
                                                               'class':'form-control',
                                                               'id':'codigo_sucursal_fk'})
                                    )
    codigo_socio_fk = EmpresasAsociadas(
                                    label='Empresa Asociada',
                                    queryset=ea_registradas,
                                    widget=forms.Select(attrs={'placeholder': 'Empresas Asociadas',
                                                               'class':'form-control',
                                                               'id':'codigo_socio_fk'})
                                    )
    

    cantidad_articulos = forms.IntegerField(label="Numero de artículos",widget=forms.NumberInput(attrs={'placeholder': 'Numero de artículos en el pedido',
        'id':'articulos','class':'form-control'}))


class DetalleForm(forms.ModelForm):
    class Meta:
        model= Detalle

        fields = ['articulo_fk','cantidad']

        

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor

        fields = ['codigo','nombre','direccion']

        widgets = {
                    'codigo': forms.TextInput(attrs={'class':'form-control',}),
                    'nombre': forms.TextInput(attrs={'class':'form-control',}),
                    'direccion': forms.TextInput(attrs={'class':'form-control',}),
        }

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['codigo','nombre','fotografia','direccion','tipo_cliente']

class AlmacenForm(forms.ModelForm):
    class Meta:
        model = Almacen
        fields = ['codigo','nombre','direccion']

class SucursalForm(forms.ModelForm):
    nuevo_codigo = Sucursal.generaCodigo()
    class Meta:
        model = Sucursal
        fields = ['codigo','nombre','direccion']

        codigo = forms.CharField(initial=Sucursal.generaCodigo())

class EmpresaAsociadaForm(forms.ModelForm):
    class Meta:
        model = EmpresaAsociada
        fields = ['codigo','nombre','direccion']

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['codigo','descripcion','monto','proveedores']
        proveedores = forms.ModelMultipleChoiceField(queryset=Proveedor.objects.all(), 
                                                required=False,),
                    
        widgets = {
                    'proveedores': forms.CheckboxSelectMultiple(),
        }