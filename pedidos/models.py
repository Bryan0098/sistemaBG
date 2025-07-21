from django.db import models

# 1. Tabla de Clientes
class Cliente(models.Model):
    id_cliente = models.IntegerField(primary_key=True)  # Respetar el ID existente
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)  # Teléfonos con 10 dígitos
    email = models.EmailField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cliente'  # Usar la tabla existente 'cliente'
        managed = False  # No gestionar la tabla

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# 2. Tabla de Proveedores
class Proveedor(models.Model):
    id_proveedor = models.IntegerField(primary_key=True)  # Respetar el ID existente
    nombre = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)  # Teléfonos con 10 dígitos
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'proveedor'  # Usar la tabla existente 'proveedor'
        managed = False  # No gestionar la tabla

    def __str__(self):
        return self.nombre

# 3. Tabla de Categorías
class Categoria(models.Model):
    id_categoria = models.IntegerField(primary_key=True)  # Respetar el ID existente
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'categoria'  # Usar la tabla existente 'categoria'
        managed = False  # No gestionar la tabla

    def __str__(self):
        return self.nombre

# 4. Tabla de Productos (Repuestos)
class Producto(models.Model):
    id_producto = models.IntegerField(primary_key=True)  # Respetar el ID existente
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    stock_minimo = models.IntegerField(default=5)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'producto'  # Usar la tabla existente 'producto'
        managed = False  # No gestionar la tabla

    def __str__(self):
        return self.nombre

# 5. Tabla de Pedidos
class Pedido(models.Model):
    id_pedido = models.IntegerField(primary_key=True)  # Respetar el ID existente
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20)  # No es necesario 'choices' ni 'default' porque MySQL maneja el ENUM
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'pedido'  # Usar la tabla existente 'pedido'
        managed = False  # No gestionar la tabla

    def __str__(self):
        return f"Pedido {self.id} - {self.estado}"

# 6. Tabla de Detalles de Pedido
class DetallePedido(models.Model):
    id_detalle = models.IntegerField(primary_key=True)  # Respetar el ID existente
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'detalle_pedido'  # Usar la tabla existente 'detalle_pedido'
        managed = False  # No gestionar la tabla

    def save(self, *args, **kwargs):
        self.subtotal = self.cantidad * self.precio_unitario
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Detalle Pedido {self.id}"
