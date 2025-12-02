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