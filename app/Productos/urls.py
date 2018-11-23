from django.urls import path
#from app.Productos.views import productos, categorias, index
from app.Productos.views import categorias, index, ViewProductos, nuevaCategoria,nuevoProducto, editarCategoria, editarProducto, eliminarCategoria, eliminarProducto, venta, prueba, create

app_name = 'productos'

urlpatterns = [
	#path('productos', productos),
	path('categorias', categorias, name="listaCategorias"),
	path('', index),
	path('index', index, name="index"),
	path('productos', ViewProductos.as_view(), name="listaProductos"),
	path('venta', venta.as_view(), name="venta"),
	path('nuevaCategoria', nuevaCategoria, name="nuevaCategoria"),
	path('editarCategoria/<idCategoria>', editarCategoria, name="editarCategoria"),
	path('eliminarCategoria/<idCategoria>', eliminarCategoria, name="eliminarCategoria"),
	path('nuevoProducto', nuevoProducto, name="nuevoProducto"),
	path('editarProducto/<idProducto>', editarProducto, name="editarProducto"),
	path('eliminarProducto/<idProducto>', eliminarProducto, name="eliminarProducto"),
	path('home/<arg1>/<arg2>', create, name='create'),
]




