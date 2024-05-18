from django.shortcuts import render
from django.contrib import messages
from .models import *

# Create your views here.
def home(request):
    return render(request,'home.html')

def dashboard(request):
    return render(request,'dashboard.html')

def productos(request):
    products = producto.objects.all()
    return render(request, 'productos.html', {'products': products})
