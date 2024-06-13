from django.db import models
from datetime import datetime, timedelta , date 

# Create your models here.
class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    descripcion =models.CharField(max_length=200)
    tipo_producto = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='imagenes/', default='imagenes/default.png')
    stock = models.IntegerField(default=0)
    fecha_vencimiento = models.DateField(default=datetime.now().date())

    def __str__(self):
        return self.nombre
    class Meta:
        db_table = 'inventarioweb_producto'


class Recepcion(models.Model):

    id = models.AutoField(primary_key=True)
    producto = models.CharField(max_length=100)
    cantidad = models.IntegerField(default=0)
    fecha = models.CharField(max_length=60)
    pasillo = models.CharField(max_length=100)
    movimiento = models.CharField(max_length=100, default=" ")

   
    def __str__(self):
        return f"{self.producto} ({self.id})"

    class Meta:
        db_table = 'inventarioweb_recepcion'



class HistorialPrecio(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, default='')
    precio = models.IntegerField(default=0)
    fecha = models.CharField(max_length=10, default='')

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'inventarioweb_HistorialPrecio'

class Envio(models.Model):

    id = models.AutoField(primary_key=True)
    producto = models.CharField(max_length=100)
    cantidad = models.IntegerField(default=0)
    fecha = models.CharField(max_length=60)
    empresa = models.CharField(max_length=100)
    movimiento = models.CharField(max_length=100, default=" ")

       
    def __str__(self):
        return f"{self.producto} ({self.id})"

    class Meta:
        db_table = 'inventarioweb_envio'


class Provedores(models.Model):
    id_provedor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    telefono = models.CharField(max_length=20)
    ciudad = models.CharField(max_length=100)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
    