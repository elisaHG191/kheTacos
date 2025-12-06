from django.db import models

class Cliente(models.Model): # (Nombre de TU MODELO o TABLA)
    
    # --- A continuación, los campos de TU FORMULARIO HTML ---
    
    nombre = models.CharField(max_length=100) 
    # (Coincide con <input name="nombre">)
    
    apellidos = models.CharField(max_length=100)
    # (Coincide con <input name="apellidos">)
    
    telefono = models.CharField(max_length=20)
    # (Coincide con <input name="telefono">)
    
    email = models.EmailField(blank=True, null=True)
    # (Coincide con <input name="email"> - Opcional)
    
    direccion = models.CharField(max_length=255)
    # (Coincide con <input name="direccion">)
    
    tacos_pref = models.CharField(max_length=50)
    # (Coincide con <select name="tacos_pref">)

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"

# --- MODELO PARA EL MENÚ ---
class Platillo(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=6, decimal_places=2) # Ejemplo: 150.50
    
    def __str__(self):
        return f"{self.nombre} - ${self.precio}"

# --- MODELO PARA LA CABECERA DE LA ORDEN ---
class Orden(models.Model):
    # Relación: Una orden pertenece a UN cliente
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE) 
    fecha = models.DateTimeField(auto_now_add=True) # Se pone la fecha sola al crearla
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Orden {self.id} - {self.cliente.nombre}"

# --- MODELO PARA LOS DETALLES (Qué comió en esa orden) ---
class DetalleOrden(models.Model):
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE)
    platillo = models.ForeignKey(Platillo, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.cantidad}x {self.platillo.nombre}"