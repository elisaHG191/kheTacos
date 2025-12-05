# kheTacos\pedidos\views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q # [IMPORTANTE] Necesario para usar "OR"
from .models import Cliente

def eliminar_cliente(request, id_cliente):
    # 1. BUSCAR: Encontramos al cliente o damos error 404 si no existe
    cliente_a_borrar = get_object_or_404(Cliente, id=id_cliente)

    # 2. CONFIRMACIÓN (POST): Si el usuario dio click en "Sí, eliminar"
    if request.method == 'POST':
        # --- AQUÍ OCURRE EL BORRADO ---
        cliente_a_borrar.delete() 
        
        # Redirigimos al buscador porque la página de este cliente ya no existe
        return redirect('buscarCliente')

    # 3. PREGUNTA (GET): Si apenas entró al link, le mostramos la advertencia
    return render(request, 'eliminar_confirmar.html', {'cliente': cliente_a_borrar})

# Nota que ahora recibimos 'id_cliente' como argumento extra
def editar_cliente(request, id_cliente):
    # 1. BUSCAR: Obtenemos el cliente específico o mostramos error 404 si no existe
    cliente_a_editar = get_object_or_404(Cliente, id=id_cliente)

    # 2. PROCESAR GUARDADO (POST)
    if request.method == 'POST':
        # Actualizamos los campos del objeto con los nuevos datos del formulario
        cliente_a_editar.nombre = request.POST['nombre']
        cliente_a_editar.apellidos = request.POST['apellidos']
        cliente_a_editar.telefono = request.POST['telefono']
        cliente_a_editar.email = request.POST['email']
        cliente_a_editar.direccion = request.POST['direccion']
        cliente_a_editar.tacos_pref = request.POST['tacos_pref']

        # Guardamos los cambios en la BD (UPDATE)
        cliente_a_editar.save()

        # Redirigimos al buscador o mostramos mensaje de éxito
        return render(request, 'editar.html', {
            'cliente': cliente_a_editar,
            'mensaje': '¡Datos actualizados correctamente!'
        })

    # 3. CARGAR FORMULARIO (GET)
    # Si apenas entramos a la página, le enviamos los datos actuales del cliente
    # para que el HTML pueda rellenar los inputs.
    return render(request, 'editar.html', {'cliente': cliente_a_editar})

def buscarCliente(request):
    # Definimos una lista vacía para evitar errores si no hay búsqueda
    resultados = [] 
    query = request.GET.get('consulta_usuario') # Obtenemos el texto del input

    # Si el usuario escribió algo...
    if query:
        # Aquí ocurre la MAGIA del "OR"
        # Buscamos: (Nombre contiene texto) O (Teléfono contiene texto)
        resultados = Cliente.objects.filter(
            Q(nombre__icontains=query) | Q(telefono__icontains=query)
        )
    
    # Enviamos los resultados al HTML
    return render(request, 'buscar.html', {'resultados': resultados})

def registroCliente(request): # (Nombre de TU FUNCIÓN VISTA)
    
    # Validamos si se enviaron datos (Si el método es POST)
    if request.method == 'POST':
        
        # --- 1. CAPTURAR DATOS DE TU HTML ---
        # Usamos request.POST['atributo_name_del_html']
        
        v_nombre = request.POST['nombre']       # (Del input name="nombre")
        v_apellidos = request.POST['apellidos'] # (Del input name="apellidos")
        v_telefono = request.POST['telefono']   # (Del input name="telefono")
        v_email = request.POST['email']         # (Del input name="email")
        v_direccion = request.POST['direccion'] # (Del input name="direccion")
        v_tacos = request.POST['tacos_pref']    # (Del select name="tacos_pref")

        # --- 2. CREAR EL OBJETO PARA LA BD ---
        cliente_nuevo = Cliente( # (Usamos TU MODELO)
            nombre=v_nombre,
            apellidos=v_apellidos,
            telefono=v_telefono,
            email=v_email,
            direccion=v_direccion,
            tacos_pref=v_tacos
        )

        # --- 3. GUARDAR EN TU BASE DE DATOS (MySQL) ---
        cliente_nuevo.save() 

        # --- 4. RESPONDER AL USUARIO ---
        return render(request, 'registroCliente.html', { # (Nombre de TU ARCHIVO HTML)
            'mensaje': '¡Cliente registrado con éxito en la BD Tacos!'
        })

    # Si es la primera vez que entra (GET), mostramos el formulario vacío
    return render(request, 'registroCliente.html') # (Nombre de TU ARCHIVO HTML)

def home(request):  # <--- TIENE QUE LLAMARSE 'home'
    context = {
        'ordenes_totales': 0,
        # ... tus otros datos ...
    }
    return render(request, 'index.html', context)

def faq(request):  # <--- TIENE QUE LLAMARSE 'home'
    return render(request, 'faq.html')

def registroOrden(request):  # <--- TIENE QUE LLAMARSE 'home'
    return render(request, 'registroOrden.html')

def contacto(request):  # <--- TIENE QUE LLAMARSE 'home'
    return render(request, 'contacto.html')

def menu(request):  # <--- TIENE QUE LLAMARSE 'home'
    return render(request, 'menu.html')

