from django.db import models

# Create your models here.
class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    descripcion =models.CharField(max_length=200)
    tipo_producto = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='imagenes/', default='imagenes/default.png')

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