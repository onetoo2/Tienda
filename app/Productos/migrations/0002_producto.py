# Generated by Django 2.1.1 on 2018-09-18 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomProducto', models.CharField(max_length=50)),
            ],
        ),
    ]
