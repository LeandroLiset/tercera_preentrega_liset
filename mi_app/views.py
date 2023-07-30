from django.shortcuts import render
from .models import Categoria, Producto, Cliente

# Create your views here.

def insertar_datos(request):
    if request.method == 'POST':
        pass
    categorias = Categoria.objects.all()
    return render(request, 'insertar_datos.html', {'categorias': categorias})

def buscar_datos(request):
    if request.method == 'POST':
        pass
    return render(request, 'buscar_datos.html')

