from dataclasses import fields
from django import forms

from app.models import Cliente,Producto,Carrito,Pedido,Soporte

class frmCliente(forms.ModelForm):
    
    class Meta:
        model=Cliente
        fields=["nombreusuario","rut","nombre","apellido","mail","suscriptor"]

class frmPerfilUsuario(forms.ModelForm):
    
    class Meta:
        model=Cliente
        fields=["rut","nombre","apellido","mail","suscriptor"]

class frmProducto(forms.ModelForm):

    class Meta:
        model=Producto
        fields=["nombre","precio","cantidad","categoria","imagen"]

class frmCantidad(forms.ModelForm):

    class Meta:
        model=Carrito
        fields=["candtidad"]

class frmEnvio(forms.ModelForm):

    class Meta:
        model=Pedido
        fields=["estado"]

class SoporteForm(forms.ModelForm):

    class Meta:
        model = Soporte
        
        fields = ["nombre","correo","asunto","mensaje"]