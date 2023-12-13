from django.shortcuts import render

# Create your views here.


from django.shortcuts import render

def productos_view(request):
    return render(request, 'productos.html')

def tiendas_view(request):
    return render(request, 'tiendas.html')

def agregar_producto_modal(request):
    return render(request, 'producto_modal.html')

def agregar_tienda_modal(request):
    return render(request, 'tienda_modal.html')

def detalle_tienda_view(request, tienda_id):
    return render(request, 'detalle_tienda.html', {'tienda_id': tienda_id})




from django.shortcuts import render, get_object_or_404
from .models import Tienda, Producto
from .forms import ProductoForm  # Necesitarás crear un formulario para agregar productos

def panel_view(request):
    tiendas = Tienda.objects.all()
    productos = Producto.objects.all()
    return render(request, 'panel.html', {'tiendas': tiendas, 'productos': productos})

def productos_view(request):
    productos = Producto.objects.all()
    return render(request, 'productos.html', {'productos': productos})

def tienda_detalle_view(request, tienda_id):
    tienda = get_object_or_404(Tienda, pk=tienda_id)
    productos_tienda = Producto.objects.filter(tienda_relacionada=tienda)
    return render(request, 'tienda_detalle.html', {'tienda': tienda, 'productos_tienda': productos_tienda})