from django.shortcuts import render, redirect
from django.views.generic import ListView
from app.Productos.models import Producto, Categoria
from app.Productos.forms import CategoriaForm, ProductoForm

# Create your views here.
'''def productos(request):
	contexto = {
	'productos': Producto.objects.all()
	}
	return render(request, 'Productos/productos.html', contexto) 
'''
def categorias(request):
	contexto = {
		'categorias': Categoria.objects.all()
	}
	return render(request, 'Productos/categorias.html', contexto) 

def index(request):
	return render(request, 'Productos/index.html')

class ViewProductos(ListView):
	model = Producto
	queryset = Producto.objects.order_by('numExist')
	template_name = 'Productos/productos.html'


def nuevaCategoria(request):
	if request.method == 'POST':
		form = CategoriaForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('productos:listaCategorias')
	else:
		form = CategoriaForm()
	return render(request, 'Productos/CategoriaForm.html',{'form': form})

def nuevoProducto(request):
	if request.method == 'POST':
		form = ProductoForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('productos:listaProductos')
	else:
		form = ProductoForm()
	return render(request, 'Productos/ProductosForm.html', {'form':form})

def editarCategoria(request, idCategoria):
	categoria = Categoria.objects.get(id = idCategoria)
	if(request.method == 'GET'):
		form = CategoriaForm(instance=categoria)
	else:
		form = CategoriaForm(request.POST, instance=categoria)
		if form.is_valid():
			form.save()
		return redirect('productos:listaCategorias')
	return render(request, 'Productos/CategoriaForm.html',{'form': form})

def editarProducto(request, idProducto):
	producto = Producto.objects.get(id = idProducto)
	if(request.method == 'GET'):
		form = ProductoForm(instance=producto)
	else:
		form = ProductoForm(request.POST, instance=producto)
		if form.is_valid():
			form.save()
		return redirect('productos:listaProductos')
	return render(request, 'Productos/ProductosForm.html', {'form':form})

def eliminarCategoria(request, idCategoria):
	categoria = Categoria.objects.get(id = idCategoria)
	if(request.method == 'GET'):
		categoria.delete()
		return redirect('productos:listaCategorias')

def eliminarProducto(request, idProducto):
	producto = Producto.objects.get(id = idProducto)
	if(request.method == 'GET'):
		producto.delete()
		return redirect('productos:listaProductos')



#https://www.agiliq.com/blog/2017/12/when-and-how-use-django-listview/