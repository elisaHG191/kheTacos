# kheTacos\pedidos\urls.py

from django.urls import path
from . import views  # Importamos las vistas de esta misma carpeta

urlpatterns = [
    # Esta ruta vacía '' significa la página principal de la app
    path('', views.home, name='home'),
    path('registro/', views.registroCliente, name='registroCliente'),
    path('buscar/', views.buscarCliente, name='buscarCliente'),
    path('editar/<int:id_cliente>/', views.editar_cliente, name='editar_cliente'),
    path('eliminar/<int:id_cliente>/', views.eliminar_cliente, name='eliminar_cliente'),
    path('faq/', views.faq, name='faq'),
    path('contacto/', views.contacto, name='contacto'),
    path('menu/nuevo/', views.crear_platillo, name='crear_platillo'),
    path('ordenes/nueva/', views.crear_orden, name='crear_orden'),
    path('ordenes/', views.lista_ordenes, name='lista_ordenes'),
]