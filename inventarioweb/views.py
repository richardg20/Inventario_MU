from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import *
from django.http import HttpResponseBadRequest

# Create your views here.
def home(request):
    return render(request,'home.html')

def dashboard(request):
    return render(request,'dashboard.html')

def productos(request):
    products = Producto.objects.all()
    low_stock_products = products.filter(stock__lte=5)
    alerta_stock = None
    alerta_vencimiento = None
    
    if low_stock_products.exists():
        alerta_stock = "Algunos productos tienen un stock bajo. Por favor, revisa los siguientes productos: " + ", ".join([product.nombre for product in low_stock_products])
    
    # Calcular la fecha actual
    fecha_actual = datetime.now().date()
    # Calcular la fecha dentro de 3 meses
    fecha_tres_meses = fecha_actual + timedelta(days=90)
    # Filtrar los productos cuya fecha de vencimiento esté dentro de los próximos 3 meses
    productos_proximo_vencimiento = products.filter(fecha_vencimiento__lte=fecha_tres_meses)
    if productos_proximo_vencimiento.exists():
        alerta_vencimiento = "Algunos productos están próximos a vencer en los próximos 3 meses."
    
    return render(request, 'productos.html', {'products': products,'alerta_stock': alerta_stock, 'alerta_vencimiento': alerta_vencimiento})



def recepcion(request, id):
    product = get_object_or_404(Producto, id=id)
    print(Producto)
    context = { "producto" : product}
    return render(request, 'recepcion.html', context)

def confirmar_recepcion(request):
    if request.method == 'POST':
        nombre2 = request.POST.get('nombre')
        cantidad2 = request.POST.get('cantidad')
        fecha2 = request.POST.get('fecha')
        pasillo2 = request.POST.get('pasillo')
        mov = 'Recepción'

        if not nombre2 or not cantidad2 or not fecha2 or not pasillo2:
            return HttpResponseBadRequest("Faltan datos en el formulario")

        try:
            cantidad2 = int(cantidad2)
        except ValueError:
            return HttpResponseBadRequest("Cantidad debe ser un número entero")

        try:
            recep = Recepcion(
                producto=nombre2,
                cantidad=cantidad2,
                fecha=fecha2,
                pasillo=pasillo2,
                movimiento = mov
            )
            recep.save()

        except Exception as e:
            return HttpResponseBadRequest(f"Error al guardar los datos: {e}")

        return redirect('productos')

    return render(request, 'productos.html')

def movimientos(request):
    recepciones = Recepcion.objects.all()
    return render(request, 'movimientos.html', {'recepciones': recepciones})

def historial(request):
    products = Producto.objects.all()
    precio = HistorialPrecio.objects.all()
    return render(request, 'historial.html', {'products': products, 'precios': precio} )

def informe(request):
    products = Producto.objects.all()
    return render(request, 'informe.html', {'products': products})
#Aca se ingresara la vista de productos
