# Generated by Django 5.0.6 on 2024-05-18 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventarioweb', '0004_rename_nombre_producto_recepcion_producto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recepcion',
            name='cantidad',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='recepcion',
            name='fecha',
            field=models.CharField(max_length=60),
        ),
    ]