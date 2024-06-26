from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import *
from django.http import HttpResponseBadRequest
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import group_required
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request,'home.html')


@login_required
def dashboard(request):

    #user_groups = request.user_groups  Obtener los grupos del usuario desde el request
    user_groups = getattr(request, 'user_groups', {})

    context = {
        'is_admin': user_groups.get('is_admin', False),
        'is_auditor': user_groups.get('is_auditor', False),
        'is_comprador': user_groups.get('is_comprador', False),
        'is_logistica': user_groups.get('is_logistica', False),
        'is_gestor': user_groups.get('is_gestor', False),
    }

    print(user_groups)
    print('------------')
    print(context)

    return render(request,'dashboard.html',context)


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
    envios = Envio.objects.all()
    recepciones = Recepcion.objects.all()
    return render(request, 'movimientos.html', {'recepciones': recepciones, "envios":envios})

def historial(request):
    products = Producto.objects.all()
    precio = HistorialPrecio.objects.all()
    return render(request, 'historial.html', {'products': products, 'precios': precio} )

def informe(request):
    products = Producto.objects.all()
    return render(request, 'informe.html', {'products': products})


def envio(request, id):
    product = get_object_or_404(Producto, id=id)
    print(Producto)
    context = { "producto" : product}
    return render(request, 'envio.html', context)

def confirmar_envio(request):
    if request.method == 'POST':
        nombre2 = request.POST.get('nombre')
        cantidad2 = request.POST.get('cantidad')
        fecha2 = request.POST.get('fecha')
        nombre_empresa = request.POST.get('empresa_seleccionada')
        
        mov = 'Envío'

        try:
            recep = Envio(
                producto=nombre2,
                cantidad=cantidad2,
                fecha=fecha2,
                empresa= nombre_empresa,
                movimiento = mov
            )
            recep.save()

        except Exception as e:
            return HttpResponseBadRequest(f"Error al guardar los datos: {e}")

        return redirect('productos')

    return render(request, 'productos.html')

def addpro(request):
    return render(request, 'addpro.html')

def confirmar_adicionpro(request):
    
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        precio = request.POST.get('precio')
        desc = request.POST.get('desc')
        stock = request.POST.get('stock')
        fechav = request.POST.get('fecha')
        tipo_pro = request.POST.get('empresa_seleccionada')
        imagen = request.FILES['imagen']

        producto = Producto(
            nombre=nombre,
            precio=precio,
            descripcion=desc,
            tipo_producto = tipo_pro,
            imagen=imagen,
            stock = stock,
            fecha_vencimiento = fechav
        )
        producto.save()

        return redirect('productos') 
    else:
        return HttpResponse('Error: Se requiere una solicitud POST')



def proveedores(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        email = request.POST.get('email', '')
        telefono = request.POST['telefono']
        ciudad = request.POST['ciudad']

        proveedor = Provedores(nombre=nombre, email=email, telefono=telefono, ciudad=ciudad)
        proveedor.save()

        return redirect('proveedores')
    
    proveedores = Provedores.objects.all()
    return render(request, 'proveedores.html', {'proveedores': proveedores})

def eliminar_proveedor(request, id_provedor):
    proveedor = get_object_or_404(Provedores, id_provedor=id_provedor)
    proveedor.delete()
    return redirect('proveedores')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'home.html', {'error': 'Nombre de usuario o contraseña incorrectos'})
    return render(request, 'home.html')
