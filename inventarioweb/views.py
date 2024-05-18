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
    return render(request, 'productos.html', {'products': products})

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