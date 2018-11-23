
var subtotal = 0;
var arreglo = [];
var productos = [];
var existencias = [];

function agregarCantidad(id,producto, costo, numExist){
	document.getElementById('cantidad').value = 0;
	mostrarPopUp('alerta');
	arreglo = [id, producto, costo, numExist];
}

function agregarCarrito(){
	cantidad = document.getElementById('cantidad').value;
	numExist = arreglo[3];

	if(cantidad <= numExist && cantidad > 0){
		quitarPopUp();
		id = arreglo[0];
		deshabilitar(id);
		producto = arreglo[1];
		costo = arreglo[2];
		tabla = document.getElementById('tablaVenta');
		monto = costo * cantidad;
		idFila = 'fila'+id;
		subtotal += monto;
		document.getElementById('total').innerHTML = "$"+subtotal;

		productos.push(id);
		existenciaFinal = numExist - cantidad;
		existencias.push(existenciaFinal);

		console.log(productos);
		console.log(existencias);

		tabla.innerHTML += "<tr scope='row' id="+idFila+">"+
								"<td>"+cantidad+"</td>"+
								"<td>"+producto+"</td>"+
								"<td>$"+costo+"</td>"+
								"<td>$"+monto+"</td>"+
								"<td>"+
									"<button class='btn' onclick='quitarCarrito("+idFila+","+monto+","+id+")'>Quitar</button>"+
								"</td>"+
							"</tr>";
	}
	else{
		esconder('alerta');
		if(cantidad > numExist){
			mostrarModal('Cantidad excede la existencia del producto.');
		}
		else{
			mostrarModal('Cantidad inválida')
		}
	}
}

function mostrarModal(texto){
	document.getElementById('textoAlerta2').innerHTML = texto;
	mostrarPopUp('alerta2');		
}


function quitarCarrito(idFila, monto, idProducto){
	tabla = document.getElementById('tablaVenta');
	tabla.removeChild(idFila);
	subtotal -= monto;
	document.getElementById('total').innerHTML = "$"+subtotal;
	habilitar(idProducto);
	for (var i = 0; i < productos.length; i++) {
		if(productos[i] == idProducto){
			productos.splice(i,1);
			existencias.splice(i, 1);
		}
	}
}

function regresarProductos(){
	return productos;
}
function regresarExistencia(){
	return existencias;
}

function mostrarPopUp(alerta){
	mostrar('popup', 'block');
	mostrar(alerta, 'flex');
}

function quitarPopUp(){
	esconder('popup');
	esconder('alerta');
	esconder('alerta2');
}

function mostrar(id, display){
	elemento = document.getElementById(id);
	elemento.style.display = display;
}

function esconder(id){
	elemento = document.getElementById(id);
	elemento.style.display = "none";
}

function habilitar(id){
	document.getElementById(id).disabled = false;
}

function deshabilitar(id){
	document.getElementById(id).disabled = true;
}
