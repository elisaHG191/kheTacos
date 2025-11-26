# kheTacos\pedidos\views.py
from django.shortcuts import render

def home(request):  # <--- TIENE QUE LLAMARSE 'home'
    context = {
        'ordenes_totales': 0,
        # ... tus otros datos ...
    }
    return render(request, 'index.html', context)