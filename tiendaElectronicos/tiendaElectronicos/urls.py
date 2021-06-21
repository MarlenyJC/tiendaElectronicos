"""tiendaElectronicos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from django.conf.urls import url,include
from rest_framework import routers
from Tienda import views


# Enrutamiento
router = routers.DefaultRouter()
#router.register(r'users',views.UserViewSet)
router.register(r'almacen',views.AlmacenViewSet)
router.register(r'sucursal',views.SucursalViewSet)
router.register(r'empresaasociada',views.EmpresaAsociadaViewSet)
router.register(r'proveedor',views.ProveedorViewSet)
router.register(r'articulo',views.ArticuloViewSet)
router.register(r'cliente',views.ClienteViewSet)
router.register(r'pedido',views.PedidoViewSet)


from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer
schema_view = get_schema_view(title='Modelos de tienda Tienda')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Tienda.urls')),
    url('docs/', schema_view, name="docs"),
    url('tienda/',include(router.urls)),
]
