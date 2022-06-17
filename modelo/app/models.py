from django.db import models
from django.forms import CharField
from distutils.command.upload import upload
from asyncio.windows_events import NULL
from datetime import datetime
# Create your models here.
estado_pedido = [
    (1, 'Preparacion'),
    (2, 'En reparto'),
    (3, 'Entregado'),
]

class Categoria(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Cliente(models.Model):
    nombreusuario=models.CharField(primary_key=True,max_length=50)
    rut=models.CharField(max_length=10)
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    mail=models.EmailField()
    suscriptor=models.BooleanField()
    
    
    
    def __str__(self):
        return "" + self.rut + " - " + self.nombre

class Producto(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50)
    precio=models.IntegerField(("Precio"))
    cantidad=models.IntegerField(("Cantidad"))
    categoria=models.ForeignKey(Categoria, on_delete=models.PROTECT)
    imagen=models.ImageField(upload_to='productoimg')
    def __str__(self):
        return self.nombre 


class Pedido(models.Model):
    id=models.AutoField(primary_key=True)
    nomusuario=models.CharField( max_length=50,default=0)
    fecha=models.DateField()
    estado=models.IntegerField(choices=estado_pedido,default=1)
    direccion=models.CharField(max_length=50)
    producto=models.ManyToManyField(Producto, through='Detalle')

    

    
class Detalle(models.Model):
    producto=models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido= models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad=models.IntegerField()

class Carrito(models.Model):
    id=models.AutoField(primary_key=True)
    idusuario=models.CharField( max_length=50)
    idprod=models.CharField( max_length=50)
    candtidad=models.IntegerField()
    precio=models.IntegerField(default=0)
    nomproduc=models.CharField(max_length=50,default=0)
    def __str__(self):
        return self.idprod

class Soporte(models.Model):
    id=models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    asunto = models.CharField(max_length=50)
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre