from django.contrib import admin

from app.models import Cliente, Detalle, Pedido, Producto, Categoria, Carrito,Soporte

# Register your models here.

class admPedido(admin.ModelAdmin):
    
    list_display=["id","fecha","direccion","estado","nomusuario"]
    
    class Meta:
        model=Pedido
        
class admCategoria(admin.ModelAdmin):
    list_display=["id","nombre"]
    class Meta:
        model=Categoria

class admProducto(admin.ModelAdmin):
    
    list_display=["id","nombre","precio","cantidad","categoria","imagen"]
    class Meta:
        model=Producto
        
        
class admDetalle(admin.ModelAdmin):
    list_display=["cantidad","pedido"]
    class Meta:
        model=Detalle

class admCliente(admin.ModelAdmin):
    list_display=["nombreusuario","rut","nombre","apellido","mail","suscriptor"]
    class Meta:
        model=Cliente

class admCarrito(admin.ModelAdmin):
    list_display=["id","idusuario","idprod","candtidad","precio","nomproduc"]
    class Meta:
        model=Carrito

class admSoporte(admin.ModelAdmin):
    
    list_display=["nombre","correo","asunto","mensaje"]
    class Meta:
        model=Soporte
        
admin.site.register(Pedido,admPedido)
admin.site.register(Producto,admProducto)  
admin.site.register(Detalle,admDetalle)      
admin.site.register(Cliente,admCliente)
admin.site.register(Categoria,admCategoria)
admin.site.register(Carrito,admCarrito)
admin.site.register(Soporte,admSoporte)
        