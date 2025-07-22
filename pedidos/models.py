from django.db import models

# 1. Tabla de Clientes
class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)  # Cambio a AutoField para Django
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cliente'
        managed = False  # No gestionar la tabla

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# 2. Tabla de Proveedores
class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)  # Cambio a AutoField
    nombre = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'proveedor'
        managed = False

    def __str__(self):
        return self.nombre

# 3. Tabla de Categorías
class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)  # Cambio a AutoField
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'categoria'
        managed = False

    def __str__(self):
        return self.nombre

# 4. Tabla de Productos (Repuestos)
class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)  # Cambio a AutoField
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    stock_minimo = models.IntegerField(default=5)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, db_column='id_categoria')
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, db_column='id_proveedor')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'producto'
        managed = False

    def __str__(self):
        return self.nombre

# 5. Tabla de Pedidos
class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)  # Cambio a AutoField
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, db_column='id_cliente')
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20)
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'pedido'
        managed = False

    def __str__(self):
        return f"Pedido {self.id_pedido}"

# 6. Tabla de Detalles de Pedido
class DetallePedido(models.Model):
    id_detalle = models.AutoField(primary_key=True)  # Cambio a AutoField
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, db_column='id_pedido')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, db_column='id_producto')
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'detalle_pedido'
        managed = False

    def save(self, *args, **kwargs):
        self.subtotal = self.cantidad * self.precio_unitario
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Detalle Pedido {self.id_detalle}"
