from django.urls import path
from . import views

urlpatterns = [
    path('insertar/', views.insertar_datos, name='insertar_datos'),
    path('buscar/', views.buscar_datos, name='buscar_datos'),
]
