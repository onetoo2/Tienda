from django import forms
from app.Productos.models import Categoria, Producto

class CategoriaForm(forms.ModelForm):

	class Meta:
		model = Categoria

		fields = {
			'nomCategoria',
			'fechaCreacion',
		}

		labels = {
			'nomCategoria': 'Categoría',
			'fechaCreacion': 'Creación',
		}

		widgets = {
			'nomCategoria' : forms.TextInput(attrs={'class': 'form-control'}),
			'fechaCreacion': forms.TextInput(attrs={'class': 'form-control'}),
		}

class ProductoForm(forms.ModelForm):

	class Meta:

		model = Producto
	
		fields = {
			'nomProducto',
			'descripcion',
			'costo',
			'disponibilidad',
			'numExist',
			'categoria',
		}

		labels = {
			'nomProducto': 'Producto',
			'descripcion': 'Descripción',
			'costo': 'Costo',
			'disponibilidad': 'Disponibilidad',
			'numExist': 'No. existencia',
			'categoria': 'Categoría',
		}

		widgets = {
			'nomProducto': forms.TextInput(attrs={'class': 'form-control'}),
			'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
			'costo': forms.TextInput(attrs={'class': 'form-control'}),
			'disponibilidad': forms.TextInput(attrs={'class': 'form-control'}),
			'numExist': forms.TextInput(attrs={'class': 'form-control'}),
			'categoria': forms.TextInput(attrs={'class': 'form-control'}),
		}