# Generated by Django 3.2.4 on 2021-06-13 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0002_remove_proveedor_direccion'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedor',
            name='direccion',
            field=models.CharField(default='', max_length=100),
        ),
    ]