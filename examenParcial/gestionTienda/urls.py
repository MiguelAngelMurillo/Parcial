from django.urls import path
from . import views

urlpatterns = [
    path('productos/', views.productos_view, name='productos'),
    path('tiendas/', views.tiendas_view, name='tiendas'),
    path('producto_modal/', views.agregar_producto_modal, name='producto_modal'),
    path('tienda_modal/', views.agregar_tienda_modal, name='tienda_modal'),
    path('detalle_tienda/<int:tienda_id>/', views.detalle_tienda_view, name='detalle_tienda'),
]



from django.urls import path
from . import views

urlpatterns = [
    path('', views.panel_view, name='panel'),
    path('productos/', views.productos_view, name='productos'),
    path('tienda/<int:tienda_id>/', views.tienda_detalle_view, name='tienda_detalle'),
    # Otras rutas y vistas necesarias
]