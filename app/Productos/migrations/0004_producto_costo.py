# Generated by Django 2.1.1 on 2018-09-18 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0003_producto_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='costo',
            field=models.IntegerField(default=0),
        ),
    ]
