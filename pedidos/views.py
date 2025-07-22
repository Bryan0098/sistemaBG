from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Cliente, Proveedor, Categoria, Producto, Pedido, DetallePedido

# Home View
def home(request):
    return render(request, 'index.html')

# ---------------------------------------------------------
# Vistas para Cliente
# ---------------------------------------------------------

def gestionar_clientes(request):
    if request.method == 'POST':
        # Crear un cliente
        if 'crear' in request.POST:
            nombre = request.POST.get('nombre')
            apellido = request.POST.get('apellido')
            telefono = request.POST.get('telefono')
            email = request.POST.get('email')
            Cliente.objects.create(
                nombre=nombre,
                apellido=apellido,
                telefono=telefono,
                email=email
            )
            messages.success(request, "Cliente creado con éxito.")

        # Actualizar un cliente
        elif 'actualizar' in request.POST:
            id_cliente = request.POST.get('id_cliente')
            cliente = get_object_or_404(Cliente, id_cliente=id_cliente)
            cliente.nombre = request.POST.get('nombre')
            cliente.apellido = request.POST.get('apellido')
            cliente.telefono = request.POST.get('telefono')
            cliente.email = request.POST.get('email')
            cliente.save()
            messages.success(request, "Cliente actualizado con éxito.")
        
        # Eliminar un cliente
        elif 'eliminar' in request.POST:
            id_cliente = request.POST.get('id_cliente')
            cliente = get_object_or_404(Cliente, id_cliente=id_cliente)
            cliente.delete()
            messages.success(request, "Cliente eliminado con éxito.")
    
    clientes = Cliente.objects.all()
    return render(request, 'gestionar_clientes.html', {'clientes': clientes})

# ---------------------------------------------------------
# Vistas para Proveedor
# ---------------------------------------------------------

def gestionar_proveedores(request):
    if request.method == 'POST':
        # Crear un proveedor
        if 'crear' in request.POST:
            nombre = request.POST.get('nombre')
            contacto = request.POST.get('contacto')
            telefono = request.POST.get('telefono')
            Proveedor.objects.create(
                nombre=nombre,
                contacto=contacto,
                telefono=telefono
            )
            messages.success(request, "Proveedor creado con éxito.")

        # Actualizar un proveedor
        elif 'actualizar' in request.POST:
            id_proveedor = request.POST.get('id_proveedor')
            proveedor = get_object_or_404(Proveedor, id_proveedor=id_proveedor)
            proveedor.nombre = request.POST.get('nombre')
            proveedor.contacto = request.POST.get('contacto')
            proveedor.telefono = request.POST.get('telefono')
            proveedor.save()
            messages.success(request, "Proveedor actualizado con éxito.")
        
        # Eliminar un proveedor
        elif 'eliminar' in request.POST:
            id_proveedor = request.POST.get('id_proveedor')
            proveedor = get_object_or_404(Proveedor, id_proveedor=id_proveedor)
            proveedor.delete()
            messages.success(request, "Proveedor eliminado con éxito.")
    
    proveedores = Proveedor.objects.all()
    return render(request, 'gestionar_proveedores.html', {'proveedores': proveedores})

# ---------------------------------------------------------
# Vistas para Categoria
# ---------------------------------------------------------

def gestionar_categorias(request):
    if request.method == 'POST':
        # Crear una categoría
        if 'crear' in request.POST:
            nombre = request.POST.get('nombre')
            descripcion = request.POST.get('descripcion')
            Categoria.objects.create(
                nombre=nombre,
                descripcion=descripcion
            )
            messages.success(request, "Categoría creada con éxito.")

        # Actualizar una categoría
        elif 'actualizar' in request.POST:
            id_categoria = request.POST.get('id_categoria')
            categoria = get_object_or_404(Categoria, id_categoria=id_categoria)
            categoria.nombre = request.POST.get('nombre')
            categoria.descripcion = request.POST.get('descripcion')
            categoria.save()
            messages.success(request, "Categoría actualizada con éxito.")
        
        # Eliminar una categoría
        elif 'eliminar' in request.POST:
            try:
                id_categoria = int(request.POST.get('id_categoria'))
                categoria = Categoria.objects.get(pk=id_categoria)
                categoria.delete()
                messages.success(request, 'Categoría eliminada correctamente.')
            except (Categoria.DoesNotExist, ValueError, TypeError):
                messages.error(request, 'Error al eliminar la categoría.')

        return redirect('gestionar_categorias')
    
    categorias = Categoria.objects.all()
    return render(request, 'gestionar_categorias.html', {'categorias': categorias})

# ---------------------------------------------------------
# Vistas para Producto
# ---------------------------------------------------------

def gestionar_productos(request):
    if request.method == 'POST':
        # Crear un producto
        if 'crear' in request.POST:
            nombre = request.POST.get('nombre')
            descripcion = request.POST.get('descripcion')
            precio = request.POST.get('precio')
            stock = request.POST.get('stock')
            stock_minimo = request.POST.get('stock_minimo')
            id_categoria = request.POST.get('categoria')  # nombre del campo debe coincidir con el de la plantilla
            id_proveedor = request.POST.get('proveedor')  # nombre del campo debe coincidir con el de la plantilla

            Producto.objects.create(
                nombre=nombre,
                descripcion=descripcion,
                precio=precio,
                stock=stock,
                stock_minimo=stock_minimo,
                categoria_id=id_categoria,  # Usando `categoria_id` para referirse a la clave foránea
                proveedor_id=id_proveedor  # Usando `proveedor_id` para referirse a la clave foránea
            )
            messages.success(request, "Producto creado con éxito.")

        # Actualizar un producto
        elif 'actualizar' in request.POST:
            id_producto = request.POST.get('id_producto')
            producto = get_object_or_404(Producto, id_producto=id_producto)
            producto.nombre = request.POST.get('nombre')
            producto.descripcion = request.POST.get('descripcion')
            producto.precio = request.POST.get('precio')
            producto.stock = request.POST.get('stock')
            producto.stock_minimo = request.POST.get('stock_minimo')
            producto.categoria_id = request.POST.get('categoria')  # Asegurando que se actualice la categoría
            producto.proveedor_id = request.POST.get('proveedor')  # Asegurando que se actualice el proveedor
            producto.save()
            messages.success(request, "Producto actualizado con éxito.")
        
        # Eliminar un producto
        elif 'eliminar' in request.POST:
            id_producto = request.POST.get('id_producto')
            producto = get_object_or_404(Producto, id_producto=id_producto)
            producto.delete()
            messages.success(request, "Producto eliminado con éxito.")
    
    # Consultar todos los productos y la lista de categorías y proveedores
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()
    proveedores = Proveedor.objects.all()

    return render(request, 'gestionar_productos.html', {
        'productos': productos,
        'categorias': categorias,
        'proveedores': proveedores
    })
# ---------------------------------------------------------
# Vistas para Pedido
# ---------------------------------------------------------

def gestionar_pedidos(request):
    if request.method == 'POST':
        # Crear un pedido
        if 'crear' in request.POST:
            id_cliente = request.POST.get('id_cliente')
            estado = request.POST.get('estado')
            total = request.POST.get('total')
            Pedido.objects.create(
                cliente_id=id_cliente,
                estado=estado,
                total=total
            )
            messages.success(request, "Pedido creado con éxito.")

        # Actualizar un pedido
        elif 'actualizar' in request.POST:
            id_pedido = request.POST.get('id_pedido')
            pedido = get_object_or_404(Pedido, id_pedido=id_pedido)
            pedido.estado = request.POST.get('estado')
            pedido.total = request.POST.get('total')
            pedido.save()
            messages.success(request, "Pedido actualizado con éxito.")
        
        # Eliminar un pedido
        elif 'eliminar' in request.POST:
            id_pedido = request.POST.get('id_pedido')
            pedido = get_object_or_404(Pedido, id_pedido=id_pedido)
            pedido.delete()
            messages.success(request, "Pedido eliminado con éxito.")
    
    pedidos = Pedido.objects.all()
    return render(request, 'gestionar_pedidos.html', {'pedidos': pedidos})

# ---------------------------------------------------------
# Vistas para Detalle de Pedido
# ---------------------------------------------------------

def gestionar_detalle_pedidos(request):
    detalles_pedido = DetallePedido.objects.all()
    pedidos = Pedido.objects.all()
    productos = Producto.objects.all()

    if request.method == 'POST':
        if 'crear' in request.POST:
            id_pedido = request.POST['id_pedido']
            id_producto = request.POST['id_producto']
            cantidad = request.POST['cantidad']
            precio_unitario = request.POST['precio_unitario']
            subtotal = float(cantidad) * float(precio_unitario)

            DetallePedido.objects.create(
                pedido_id=id_pedido,
                producto_id=id_producto,
                cantidad=cantidad,
                precio_unitario=precio_unitario,
                subtotal=subtotal
            )
            return redirect('gestionar_detalle_pedidos')

        if 'actualizar' in request.POST:
            id_detalle = request.POST['id_detalle']
            id_pedido = request.POST['id_pedido']
            id_producto = request.POST['id_producto']
            cantidad = request.POST['cantidad']
            precio_unitario = request.POST['precio_unitario']
            subtotal = float(cantidad) * float(precio_unitario)

            detalle = DetallePedido.objects.get(id_detalle=id_detalle)
            detalle.pedido_id = id_pedido
            detalle.producto_id = id_producto
            detalle.cantidad = cantidad
            detalle.precio_unitario = precio_unitario
            detalle.subtotal = subtotal
            detalle.save()
            return redirect('gestionar_detalle_pedidos')

        if 'eliminar' in request.POST:
            id_detalle = request.POST['id_detalle']
            DetallePedido.objects.get(id_detalle=id_detalle).delete()
            return redirect('gestionar_detalle_pedidos')

    return render(request, 'gestionar_detalle_pedidos.html', {
        'detalles_pedido': detalles_pedido,
        'pedidos': pedidos,
        'productos': productos
    })