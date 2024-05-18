from django.db import models

# Create your models here.
class producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    descripcion =models.CharField(max_length=200)
    tipo_producto = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='imagenes/', default='imagenes/default.png')

    def __str__(self):
        return self.nombre