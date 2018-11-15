from django.db import models

# Create your models here.

class Categoria(models.Model):
	nomCategoria = models.CharField(max_length=50)
	fechaCreacion = models.DateField(default='2018-09-10')

class Producto(models.Model):
	nomProducto = models.CharField(max_length=50)
	descripcion = models.CharField(max_length=250, default='')
	costo = models.IntegerField(default=0)
	disponibilidad = models.BooleanField(default=False)
	numExist = models.IntegerField(default=0)
	categoria = models.ForeignKey(Categoria, null=True, blank=True, on_delete=models.CASCADE)



