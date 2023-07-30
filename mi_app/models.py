from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    class Meta:
        app_label = 'mi_app'


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    class Meta:
        app_label = 'mi_app'

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    class Meta:
        app_label = 'mi_app'