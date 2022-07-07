from rest_framework import serializers
from .models import *

class ClienteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Cliente
        fields=["nombreusuario","rut","nombre","apellido","mail","suscriptor"]

class PerfilUsuarioSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Cliente
        fields=["rut","nombre","apellido","mail","suscriptor"]

class ProductoSerializer(serializers.ModelSerializer):

    class Meta:
        model=Producto
        fields=["nombre","precio","cantidad","categoria","imagen"]

class CantidadSerializer(serializers.ModelSerializer):

    class Meta:
        model=Carrito
        fields=["candtidad"]

class PedidoSerializer(serializers.ModelSerializer):

    class Meta:
        model=Pedido
        fields=["nomusuario","fecha","estado","direccion","producto"]

class SoporteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Soporte
        
        fields = ["nombre","correo","asunto","mensaje"]