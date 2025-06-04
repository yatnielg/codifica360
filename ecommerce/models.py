from django.db import models
from django.contrib.auth.models import User

# Create your models here.
########################################################################################################################################
class Negocio(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    subdominio = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_payment_date = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    social_media = models.JSONField(blank=True, null=True)  # Store social media links as JSON
    owner = models.CharField(max_length=100, blank=True, null=True)  # Owner's name

    def __str__(self):
        return self.nombre

########################################################################################################################################
class Cliente(models.Model):
    from pais.models import State, Municipality, Country  # Importamos los modelos de ubicación
    negocio = models.ForeignKey(Negocio, on_delete=models.CASCADE)  # Negocio al que pertenece el cliente
    user = models.OneToOneField(User, on_delete=models.CASCADE)    
    first_name = models.CharField(max_length=30, blank=True, null=True)  # First name of the user
    last_name = models.CharField(max_length=30, blank=True, null=True)    
    second_last_name = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)        
    phone = models.CharField(max_length=20, blank=True, null=True)
    phone_secondary = models.CharField(max_length=20, blank=True, null=True)  # Secondary phone number    
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)        
    country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, null=True)  # Country of the user
    state = models.ForeignKey(State, on_delete=models.CASCADE, blank=True, null=True)  # State of the user
    municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE, blank=True, null=True)  # Municipality of the user
    address = models.TextField(blank=True, null=True)    
    apartment = models.CharField(max_length=50, blank=True, null=True)  # Apartment or unit number
    zip_code = models.CharField(max_length=20, blank=True, null=True)
    last_login = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)  # To track if the user has superuser privileges
    is_staff = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)  # To track if the user has verified their email
    is_guest = models.BooleanField(default=False)  # To track if the user is a guest
    is_blocked = models.BooleanField(default=False)  # To track if the user is blocked
    is_deleted = models.BooleanField(default=False)  # To track if the user account is deleted
    is_newsletter_subscribed = models.BooleanField(default=False)  # To track if the user is subscribed to the newsletter
    is_marketing_consent = models.BooleanField(default=False)  # To track if the user has given consent for marketing communications
    is_activated = models.BooleanField(default=False)  # To track if the user account is activated
    is_deactivated = models.BooleanField(default=False)  # To track if the user account is deactivated
    is_anonymous = models.BooleanField(default=False)  # To track if the user is anonymous
    is_authenticated = models.BooleanField(default=False)  # To track if the user is authenticated
    is_premium = models.BooleanField(default=False)  # To track if the user has a premium account
    is_trial = models.BooleanField(default=False)  # To track if the user is on a trial period
    newsletter_subscription = models.BooleanField(default=False)  # To track if the user is subscribed to the newsletter    
    marketing_consent = models.BooleanField(default=False)  # To track if the user has given consent for marketing communications
    birth_date = models.DateField(blank=True, null=True)
    referring_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='referred_users')  # User who referred this user

    def __str__(self):
        return self.user.username

########################################################################################################################################
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    negocio = models.ForeignKey(Negocio, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='subcategories')

    def __str__(self):
        return self.name

########################################################################################################################################
class Supplier(models.Model):
    name = models.CharField(max_length=100, unique=True)
    contact = models.CharField(max_length=100, blank=True, null=True)  # Persona de contacto
    phone = models.CharField(max_length=20, blank=True, null=True)  # Teléfono del proveedor
    email = models.EmailField(blank=True, null=True)  # Correo del proveedor
    address = models.TextField(blank=True, null=True)  # Dirección física
    negocio = models.ForeignKey(Negocio, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
########################################################################################################################################
class Product(models.Model):
    sku = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)    
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    previous_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Previous price before discount
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    stock = models.PositiveIntegerField(default=0)  # Stock quantity
    reservation = models.PositiveIntegerField(default=0)  # Reserved stock quantity
    negocio = models.ForeignKey(Negocio, on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Product weight
    dimensions = models.JSONField(blank=True, null=True)  # Store product dimensions as JSON
    size = models.CharField(max_length=50, blank=True, null=True)  # Product size
    color = models.CharField(max_length=50, blank=True, null=True)  # Product color
    order = models.PositiveIntegerField(default=0)  # Product order in the catalog
    sold = models.PositiveIntegerField(default=0)  # Quantity sold
    broken = models.PositiveIntegerField(default=0)  # Quantity broken
    gift = models.PositiveIntegerField(default=0)  # Quantity gifted    
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, blank=True) # Supplier name

    def __str__(self):
        return self.name
########################################################################################################################################
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="imagenes")
    image = models.ImageField(upload_to="products/")
    descripcion = models.TextField(blank=True, null=True)  # Opcional para describir la imagen
    fecha_subida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Imagen de {self.product.nombre}"
########################################################################################################################################
class Warehouses(models.Model):
    from pais.models import State, Municipality, Country  # Importamos los modelos de ubicación
    negocio = models.ForeignKey(Negocio, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)    
    order = models.PositiveIntegerField(default=0)
    gestor_almacen = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='gestor_almacenes')  # Usuario que gestiona el almacén
    # Definimos la ubicación del almacén
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    estado = models.ForeignKey(State, on_delete=models.CASCADE, blank=True, null=True)
    municipio = models.ForeignKey(Municipality, on_delete=models.CASCADE, blank=True, null=True)
    support_transfer = models.BooleanField(default=False)  # Si el almacén soporta transferencias entre almacenes
    is_primary = models.BooleanField(default=False)
    capacity = models.PositiveIntegerField(default=0)  # Capacidad máxima del almacén

    def __str__(self):
        return f"{self.nombre} ({self.estado if self.estado else self.municipio})"
########################################################################################################################################    
class WarehousesProduct(models.Model):
    warehouse = models.ForeignKey(Warehouses, on_delete=models.CASCADE, related_name='warehouse_products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)  # Cantidad de producto en el almacén
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación del registro
    updated_at = models.DateTimeField(auto_now=True)  # Fecha de actualización del registro
    is_active = models.BooleanField(default=True)  # Indica si el producto está activo en el almacén
    reserved_quantity = models.PositiveIntegerField(default=0)  # Cantidad reservada del producto en el almacén 
    broken_quantity = models.PositiveIntegerField(default=0)  # Cantidad rota del producto en el almacén
    gift_quantity = models.PositiveIntegerField(default=0)  # Cantidad de producto regalado en el almacén


    class Meta:
        unique_together = ('warehouse', 'product')  # Un producto no puede estar duplicado en el mismo almacén

    def __str__(self):
        return f"{self.product.name} en {self.warehouse.nombre} ({self.quantity})"
    
########################################################################################################################################    
class Role(models.Model):
    nombre = models.CharField(max_length=100, unique=True)  # Cargo en la empresa (Ej: Director, Almacén, Vendedor)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre
########################################################################################################################################
class Earnings(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)  # Cargo que recibe el pago
    categoria = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)  # Categoría si no hay producto
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)  # Producto específico    
    monto = models.DecimalField(max_digits=10, decimal_places=2)  # Cantidad de dinero que gana

    def __str__(self):
        return f"{self.role.nombre} - {self.monto} ({self.product.nombre if self.product else self.categoria.name})"

########################################################################################################################################
class SalesOrder(models.Model):
    negocio = models.ForeignKey(Negocio, on_delete=models.CASCADE)  # Tienda que vende los productos
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación de la orden
    updated_at = models.DateTimeField(auto_now=True)  # Fecha de actualización de la orden
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)  # Cliente que realiza la orden   
    warehouses_origen = models.ForeignKey(Warehouses, on_delete=models.CASCADE, related_name="ordenes_origen")
    warehouses_destino = models.ForeignKey(Warehouses, on_delete=models.CASCADE, related_name="ordenes_destino")
    estado = models.CharField(
    max_length=50,
    choices=[
        ("Pendiente", "Pendiente"),
        ("Procesando", "Procesando"),
        ("Enviado", "Enviado"),
        ("Vendido", "Vendido"),
        ("Completado", "Completado"),
    ]
    )
    motivo_salida = models.CharField(
    max_length=50,
    choices=[
        ("Venta", "Venta"),
        ("Roto", "Roto"),
        ("Regalo", "Regalo"),
    ],
    blank=True, null=True  # Permite pedidos sin motivo si aún no se ha definido
    )
    
    shipping_address = models.TextField(blank=True, null=True)  # Dirección de envío
    billing_address = models.TextField(blank=True, null=True)  # Dirección de facturación
    payment_method = models.CharField(max_length=50, blank=True, null=True)  # Método de pago utilizado
    shipping_method = models.CharField(max_length=50, blank=True, null=True)  # Método de envío utilizado
    tracking_number = models.CharField(max_length=100, blank=True, null=True)  # Número de seguimiento del envío
    is_paid = models.BooleanField(default=False)  # Indica si la orden ha sido pagada
    is_refunded = models.BooleanField(default=False)  # Indica si la orden ha sido reembolsada
    is_returned = models.BooleanField(default=False)  # Indica si la orden ha sido devuelta
    is_gift = models.BooleanField(default=False)  # Indica si la orden es un regalo
    gestor_orden = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='gestor_ordenes')  # Usuario que gestiona la orden
    comment = models.TextField(blank=True, null=True)  # Comentario opcional sobre la orden


    def __str__(self):
        return f"Orden {self.id} - {self.negocio.nombre} ({self.estado})"
########################################################################################################################################
class SalesOrderItem(models.Model):
    sales_order = models.ForeignKey(SalesOrder, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre} ({self.orden})"
########################################################################################################################################
class InventoryTransfer(models.Model):    
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    origen = models.ForeignKey(Warehouses, on_delete=models.CASCADE, related_name="envios")
    destino = models.ForeignKey(Warehouses, on_delete=models.CASCADE, related_name="recepciones")
    comment = models.TextField(blank=True, null=True)  # Comentario opcional sobre la transferencia
    cantidad = models.PositiveIntegerField()
    fecha_transferencia = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(
    max_length=50,
    choices=[
        ("Pendiente", "Pendiente"),
        ("Completado", "Completado"),
        ("Devuelto", "Devuelto"),  # Pedido regresado porque nunca se envió correctamente
    ]
)

    def __str__(self):
        return f"Transferencia {self.id} ({self.origen.nombre} → {self.destino.nombre})"
########################################################################################################################################
class ProductExchange(models.Model):        
    producto_original = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="original")
    product_delivered = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="delivered")
    warehouses_product = models.ForeignKey(WarehousesProduct, on_delete=models.CASCADE, related_name="exchanges")
    comment = models.TextField(blank=True, null=True)  # Comentario opcional sobre el cambio
    cantidad = models.PositiveIntegerField(default=1)
    fecha_cambio = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(
        max_length=50,
        choices=[
            ("Pendiente", "Pendiente"),
            ("Completado", "Completado"),
            ("Cancelado", "Cancelado"),
        ],
        default="Pendiente",
    )

    def __str__(self):
        return f"Cambio en Orden {self.orden.id}: {self.producto_original.nombre} → {self.producto_entregado.nombre}"
########################################################################################################################################
class Discount(models.Model):
    nombre = models.CharField(max_length=100)  # Nombre del descuento
    codigo = models.CharField(max_length=50, unique=True, blank=True, null=True)  # Código promocional opcional
    porcentaje = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)  # % de descuento
    monto_fijo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Descuento fijo en dinero
    global_discount = models.BooleanField(default=False)  # Si es descuento para todos los productos
    activo = models.BooleanField(default=True)  # Si el descuento está habilitado
    fecha_inicio = models.DateTimeField(blank=True, null=True)  # Cuándo inicia la promoción
    fecha_fin = models.DateTimeField(blank=True, null=True)  # Cuándo expira el descuento
    comment = models.TextField(blank=True, null=True)  # Comentario opcional sobre el descuento

    def __str__(self):
        tipo = "Global" if self.global_discount else "Código" if self.codigo else "Por producto"
        return f"{self.nombre} ({tipo})"
########################################################################################################################################
class StockEntry(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Producto que entra al sistema
    cantidad = models.PositiveIntegerField()  # Cantidad de unidades ingresadas
    almacen = models.ForeignKey(Warehouses, on_delete=models.CASCADE)  # Almacén donde se recibe
    comment = models.TextField(blank=True, null=True)  # Comentario opcional sobre la entrada
    proveedor = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, blank=True)  # Quién suministró el producto
    fecha_ingreso = models.DateTimeField(auto_now_add=True)  # Fecha automática al ingresar el producto
    motivo_ingreso = models.CharField(
        max_length=50,
        choices=[
            ("Producción", "Producción"),
            ("Compra", "Compra"),            
            ("Devolución", "Devolución"),
            ("Donación", "Donación"),
        ]
    )

    def __str__(self):
        return f"{self.product.name} ({self.cantidad} unidades en {self.almacen.name})"
########################################################################################################################################
class StockExit(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Producto que sale del sistema
    cantidad = models.PositiveIntegerField()  # Cantidad de unidades salientes
    almacen = models.ForeignKey(Warehouses, on_delete=models.CASCADE)  # Almacén desde donde se retira
    comment = models.TextField(blank=True, null=True)  # Comentario opcional sobre la salida
    fecha_salida = models.DateTimeField(auto_now_add=True)  # Fecha automática al retirar el producto
    motivo_salida = models.CharField(
        max_length=50,
        choices=[
            ("Venta", "Venta"),
            ("Roto", "Roto"),
            ("Regalo", "Regalo"),
            ("Devolución", "Devolución"),
        ]
    )

    def __str__(self):
        return f"{self.product.name} ({self.cantidad} unidades saliendo de {self.almacen.name})"