from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import *
from django.utils import timezone
from datetime import datetime
from decimal import Decimal

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
            stock_minimo = 5
            id_categoria = request.POST.get('categoria')
            id_proveedor = request.POST.get('proveedor')

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
            producto.stock_minimo = 5
            producto.categoria_id = request.POST.get('categoria')
            producto.proveedor_id = request.POST.get('proveedor')
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
                total=total,
                fecha=timezone.now(),  # Fecha del día de hoy
                fecha_creacion=timezone.now(),
                fecha_actualizacion=timezone.now()
            )
            messages.success(request, "Pedido creado con éxito.")

        # Actualizar un pedido
        elif 'actualizar' in request.POST:
            id_pedido = request.POST.get('id_pedido')
            pedido = get_object_or_404(Pedido, id_pedido=id_pedido)
            pedido.estado = request.POST.get('estado')
            pedido.total = request.POST.get('total')
            pedido.fecha_actualizacion = timezone.now()  # Se actualiza con la fecha actual
            pedido.save()
            messages.success(request, "Pedido actualizado con éxito.")

        # Eliminar un pedido
        elif 'eliminar' in request.POST:
            id_pedido = request.POST.get('id_pedido')
            pedido = get_object_or_404(Pedido, id_pedido=id_pedido)
            pedido.delete()
            messages.success(request, "Pedido eliminado con éxito.")

    pedidos = Pedido.objects.select_related('cliente').all()
    clientes = Cliente.objects.all()
    return render(request, 'gestionar_pedidos.html', {
        'pedidos': pedidos,
        'clientes': clientes
    })

# ---------------------------------------------------------
# Vistas para Detalle de Pedido
# ---------------------------------------------------------

def gestionar_detalle_pedidos(request):
    detalles_pedido = DetallePedido.objects.all()
    pedidos = Pedido.objects.all()
    productos = Producto.objects.all()

    if request.method == 'POST':
        if 'crear' in request.POST:
            try:
                id_pedido = int(request.POST['id_pedido'])
                id_producto = int(request.POST['id_producto'])
                cantidad = int(request.POST['cantidad'])
                precio_unitario = float(request.POST['precio_unitario'])
                subtotal = cantidad * precio_unitario

                DetallePedido.objects.create(
                    pedido_id=id_pedido,
                    producto_id=id_producto,
                    cantidad=cantidad,
                    precio_unitario=precio_unitario,
                    subtotal=subtotal
                )
            except (ValueError, TypeError) as e:
                print(f"Error al crear detalle: {e}")
            return redirect('gestionar_detalle_pedidos')

        if 'actualizar' in request.POST:
            try:
                id_detalle = int(request.POST['id_detalle'])
                id_pedido = int(request.POST['id_pedido'])
                id_producto = int(request.POST['id_producto'])
                cantidad = int(request.POST['cantidad'])
                precio_unitario = float(request.POST['precio_unitario'])
                subtotal = cantidad * precio_unitario

                detalle = DetallePedido.objects.get(id_detalle=id_detalle)
                detalle.pedido_id = id_pedido
                detalle.producto_id = id_producto
                detalle.cantidad = cantidad
                detalle.precio_unitario = precio_unitario
                detalle.subtotal = subtotal
                detalle.save()
            except (ValueError, TypeError, DetallePedido.DoesNotExist) as e:
                print(f"Error al actualizar detalle: {e}")
            return redirect('gestionar_detalle_pedidos')

        if 'eliminar' in request.POST:
            try:
                id_detalle = int(request.POST['id_detalle'])
                DetallePedido.objects.get(id_detalle=id_detalle).delete()
            except DetallePedido.DoesNotExist:
                print("Detalle no encontrado para eliminar.")
            return redirect('gestionar_detalle_pedidos')

    return render(request, 'gestionar_detalle_pedidos.html', {
        'detalles_pedido': detalles_pedido,
        'pedidos': pedidos,
        'productos': productos
    })



def convert_to_serializable(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    elif isinstance(obj, list):
        return [convert_to_serializable(i) for i in obj]
    elif isinstance(obj, dict):
        return {k: convert_to_serializable(v) for k, v in obj.items()}
    else:
        return obj
from django.shortcuts import render
from django.db import connection
import json
from decimal import Decimal

def convert_to_serializable(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    elif isinstance(obj, list):
        return [convert_to_serializable(i) for i in obj]
    elif isinstance(obj, dict):
        return {k: convert_to_serializable(v) for k, v in obj.items()}
    else:
        return obj

def charts(request):
    with connection.cursor() as cursor:

        # Pedidos por Mes
        cursor.execute("""
            SELECT MONTHNAME(fecha) AS mes, COUNT(*) AS total
            FROM pedido
            WHERE fecha >= CURDATE() - INTERVAL 6 MONTH
            GROUP BY MONTH(fecha), MONTHNAME(fecha)
            ORDER BY MONTH(fecha)
        """)
        pedidos_data = cursor.fetchall()
        pedidos_labels = [row[0] for row in pedidos_data]
        pedidos_values = [row[1] for row in pedidos_data]

        # Ventas por Mes
        cursor.execute("""
            SELECT MONTHNAME(fecha) AS mes, SUM(total) AS total
            FROM pedido
            WHERE fecha >= CURDATE() - INTERVAL 6 MONTH
            GROUP BY MONTH(fecha), MONTHNAME(fecha)
            ORDER BY MONTH(fecha)
        """)
        ventas_data = cursor.fetchall()
        ventas_labels = [row[0] for row in ventas_data]
        ventas_values = [row[1] for row in ventas_data]

        # Pedidos por Día
        cursor.execute("""
            SELECT DATE_FORMAT(fecha, '%%e de %%M') AS dia, COUNT(*) AS total
            FROM pedido
            WHERE fecha >= CURDATE() - INTERVAL 15 DAY
            GROUP BY DATE(fecha)
            ORDER BY DATE(fecha)
        """)
        pedidos_dia_data = cursor.fetchall()
        pedidos_dia_labels = [row[0] for row in pedidos_dia_data]
        pedidos_dia_values = [row[1] for row in pedidos_dia_data]

        # Clientes Nuevos por Mes
        cursor.execute("""
            SELECT MONTHNAME(fecha_creacion) AS mes, COUNT(*) AS total
            FROM cliente
            WHERE fecha_creacion >= CURDATE() - INTERVAL 6 MONTH
            GROUP BY MONTH(fecha_creacion), MONTHNAME(fecha_creacion)
            ORDER BY MONTH(fecha_creacion)
        """)
        clientes_data = cursor.fetchall()
        clientes_labels = [row[0] for row in clientes_data]
        clientes_values = [row[1] for row in clientes_data]

        # Pedidos por Estado
        cursor.execute("""
            SELECT estado, COUNT(*) AS total
            FROM pedido
            GROUP BY estado
        """)
        estado_data = cursor.fetchall()
        estado_labels = [row[0] for row in estado_data]
        estado_values = [row[1] for row in estado_data]

        # Top Productos Vendidos
        cursor.execute("""
            SELECT p.nombre, SUM(dp.cantidad) AS total
            FROM detalle_pedido dp
            JOIN producto p ON dp.id_producto = p.id_producto
            GROUP BY p.id_producto
            ORDER BY total DESC
            LIMIT 5
        """)
        productos_data = cursor.fetchall()
        productos_labels = [row[0] for row in productos_data]
        productos_values = [row[1] for row in productos_data]

        # Categorías con más productos
        cursor.execute("""
            SELECT c.nombre, COUNT(p.id_producto) AS total
            FROM categoria c
            JOIN producto p ON c.id_categoria = p.id_categoria
            GROUP BY c.id_categoria
            ORDER BY total DESC
            LIMIT 5
        """)
        categorias_data = cursor.fetchall()
        categorias_labels = [row[0] for row in categorias_data]
        categorias_values = [row[1] for row in categorias_data]

        # Clientes Top
        cursor.execute("""
            SELECT CONCAT(c.nombre, ' ', c.apellido), SUM(p.total) AS total
            FROM cliente c
            JOIN pedido p ON p.id_cliente = c.id_cliente
            GROUP BY c.id_cliente
            ORDER BY total DESC
            LIMIT 5
        """)
        clientes_top_data = cursor.fetchall()
        clientes_top_labels = [row[0] for row in clientes_top_data]
        clientes_top_values = [row[1] for row in clientes_top_data]

        # Proveedores más usados
        cursor.execute("""
            SELECT pr.nombre, COUNT(p.id_producto)
            FROM proveedor pr
            JOIN producto p ON p.id_proveedor = pr.id_proveedor
            GROUP BY pr.id_proveedor
            ORDER BY COUNT(p.id_producto) DESC
            LIMIT 5
        """)
        proveedores_data = cursor.fetchall()
        proveedores_labels = [row[0] for row in proveedores_data]
        proveedores_values = [row[1] for row in proveedores_data]

        # Productos con menor stock
        cursor.execute("""
            SELECT nombre, stock
            FROM producto
            ORDER BY stock ASC
            LIMIT 5
        """)
        stock_data = cursor.fetchall()
        stock_labels = [row[0] for row in stock_data]
        stock_values = [row[1] for row in stock_data]

    return render(request, 'charts.html', {
        'pedidos_labels': json.dumps(pedidos_labels),
        'pedidos_values': json.dumps(convert_to_serializable(pedidos_values)),
        'ventas_labels': json.dumps(ventas_labels),
        'ventas_values': json.dumps(convert_to_serializable(ventas_values)),
        'pedidos_dia_labels': json.dumps(pedidos_dia_labels),
        'pedidos_dia_values': json.dumps(convert_to_serializable(pedidos_dia_values)),
        'clientes_labels': json.dumps(clientes_labels),
        'clientes_values': json.dumps(convert_to_serializable(clientes_values)),
        'estado_labels': json.dumps(estado_labels),
        'estado_values': json.dumps(convert_to_serializable(estado_values)),
        'productos_labels': json.dumps(productos_labels),
        'productos_values': json.dumps(convert_to_serializable(productos_values)),
        'categorias_labels': json.dumps(categorias_labels),
        'categorias_values': json.dumps(convert_to_serializable(categorias_values)),
        'clientes_top_labels': json.dumps(clientes_top_labels),
        'clientes_top_values': json.dumps(convert_to_serializable(clientes_top_values)),
        'proveedores_labels': json.dumps(proveedores_labels),
        'proveedores_values': json.dumps(convert_to_serializable(proveedores_values)),
        'stock_labels': json.dumps(stock_labels),
        'stock_values': json.dumps(convert_to_serializable(stock_values)),
    })
