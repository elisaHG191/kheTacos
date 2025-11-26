# kheTacos\pedidos\urls.py

from django.urls import path
from . import views  # Importamos las vistas de esta misma carpeta

urlpatterns = [
    # Esta ruta vacía '' significa la página principal de la app
    path('', views.home, name='home'),
]