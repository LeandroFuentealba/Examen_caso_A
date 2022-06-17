from datetime import datetime
from django.shortcuts import get_object_or_404,redirect, render
from app.forms import frmCliente,frmPerfilUsuario,frmProducto,frmCantidad,frmEnvio,SoporteForm
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required,permission_required

from app.models import Cliente, Carrito, Producto, Pedido, Detalle, Soporte


# Create your views here.
def index (request): 
    return render(request,"app/index.html")
def roedor (request): 
    roedores=Producto.objects.filter(categoria="3")
    
    contexto={
        "roedores":roedores
    }
    
    return render(request,"app/roedor.html",contexto)
def perro (request): 
    perros=Producto.objects.filter(categoria="1")
    
    contexto={
        "perros":perros
    }
    
    return render(request,"app/perro.html",contexto)
def gatos (request): 
    gatos=Producto.objects.filter(categoria="5")
    
    contexto={
        "gatos":gatos
    }
    
    return render(request,"app/gatos.html",contexto)
def aves (request): 
    aves=Producto.objects.filter(categoria="6")
    
    contexto={
        "aves":aves
    }
    
    return render(request,"app/aves.html",contexto)
def anfibios (request): 
    anfibios=Producto.objects.filter(categoria="7")
    
    contexto={
        "anfibios":anfibios
    }
    
    return render(request,"app/anfibios.html",contexto)
def quienes (request): 
    return render(request,"app/quienes.html")
@login_required()
def perfil (request): 
    perfil=Cliente.objects.filter(nombreusuario=request.user)
    pedido=Pedido.objects.filter(nomusuario=request.user)
    contexto={
        "perfil":perfil,
        "pedido":pedido,
    }
    
    return render(request,"app/perfil.html",contexto)
@login_required()
def carrito (request):
    total=0
    carritos=Carrito.objects.filter(idusuario=request.user)
    for item in carritos:
        total= total+item.precio
    contexto={
        "carritos":carritos,
        "total":total  
    }
    
    return render(request,"app/carrito.html",contexto)

@login_required()
def eliminarproductocarrito(request,id):
    carrito=get_object_or_404(Carrito,id=id)

    carrito.delete()

    return redirect(to="carrito")

def crearperfil(request):
    cli=Cliente()
    cli.nombreusuario=request.user.username
    cli.apellido="soto"
    cli.nombre="wacoldo"
    cli.mail="wacolodomail"
    cli.rut="123456"
    cli.suscriptor=True
    cli.save()
    return render(request,"app/crearperfil.html")

def crearcategoria(request):
    cat=Categoria()
    cat.id=1
    cat.nombre="perros"
    cat.save()
    return render(request,"app/crearperfil.html")
@login_required()
def listadocarrito(request):
    carrito=Carrito.objects.all()
    contexto={
        "carrito":carrito
    }
    return render(request,"app/carrito.html",contexto)

# Crud usuario
@permission_required('change_soporte')
def listado(request):
    cliente=Cliente.objects.all()
    total=Cliente.objects.count()
    contexto={
        "cliente":cliente,
        "total":total
    }
    return render(request,"app/listado.html",contexto)
@permission_required('change_soporte')
def crear(request):
    formulario=frmCliente(request.POST or None)
    
    contexto={
        "frm":formulario
    }
    
    if request.method=="POST":
        formulario=frmCliente(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listado")
    
   
    
    return render(request,"app/crear.html",contexto)
@permission_required('change_soporte')
def modificar(request,id):
    cliente=get_object_or_404(Cliente,nombreusuario=id)
    
    frm=frmCliente(instance=cliente)
    contexto={
        "frm":frm,
        "id":id
    }
    
    if request.method=="POST":
        frm=frmCliente(data=request.POST,instance=cliente)
        if frm.is_valid():
            cliente_mod=Cliente.objects.get(nombreusuario=cliente.nombreusuario)
            datos=frm.cleaned_data
            cliente_mod.nombre=datos.get("nombre")
            cliente_mod.apellido=datos.get("apellido")
            cliente_mod.mail=datos.get("mail")
            cliente_mod.save()
            return redirect(to="listado")
            
        
        
    return render(request,"app/modificar.html",contexto)
@permission_required('change_soporte')
def eliminar(request,id):
    cliente_tokill=get_object_or_404(Cliente,nombreusuario=id)
    contexto={
        "cliente":cliente_tokill
    }
    
    if request.method=="POST":
        cliente_tokill.delete()
        return redirect(to="listado")
    
    
    return render(request,"app/eliminar.html",contexto)

# creacion de perfil de usuario
@login_required()
def cambiarpassword(request):
    form=PasswordChangeForm(request.POST or None)
    contexto={
        "form":form
    }
    
    if request.method=="POST":
        form=PasswordChangeForm(request.user,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="index")
    
    return render(request,"registration/cambiarpassword.html",contexto)

def registro(request):
    form=UserCreationForm(request.POST or None)
    contexto={
        "form":form
    }
    
    if request.method=="POST":
        form=UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            credenciales=authenticate(username=form.cleaned_data["username"],password=form.cleaned_data["password1"])
            login(request,credenciales)
            return redirect(to="perfilusuario")
    
    return render(request,"registration/registro.html",contexto)

def perfilusuario(request):
    form=frmPerfilUsuario(request.POST or None)
    
    contexto={
        "form":form
    }
    if request.method=="POST":
        form=frmPerfilUsuario(data=request.POST)
        if form.is_valid():
            datos=form.cleaned_data
            perfil=Cliente()
            perfil.rut=datos.get("rut")
            perfil.nombre=datos.get("nombre")
            perfil.apellido=datos.get("apellido")
            perfil.mail=datos.get("mail")
            perfil.suscriptor=datos.get("suscriptor")
            perfil.nombreusuario=request.user.username
            perfil.save()
            
            
            
            return redirect(to="index")
    
    
    return render(request,"registration/perfilusuario.html",contexto)

# Crud productos
@permission_required('change_soporte')
def listaproductos(request):
    lista=Producto.objects.all()
    totalp=Producto.objects.count()
    contexto={
        "productos":lista,
        "totalp":totalp
    }
    return render(request,"app/listaproductos.html",contexto)
@permission_required('change_soporte')
def modificarproductos(request,id):
    producto=get_object_or_404(Producto,id=id)
    
    form=frmProducto(instance=producto)
  
    contexto={
        "form":form
    }
    
    if request.method=="POST":
        form=frmProducto(data=request.POST,instance=producto)
        
        if form.is_valid():
            datos=form.cleaned_data
            produ=Producto.objects.get(id=id)
 
            produ.nombre=datos.get("nombre")
            produ.precio=datos.get("precio")
            produ.cantidad=datos.get("cantidad")
            produ.categoria=datos.get("categoria")
            produ.imagen=datos.get("imagen")
            produ.save()
            return redirect(to="listaproductos")
      
            
    return render(request,"app/modificarproductos.html",contexto)
@permission_required('change_soporte')
def eliminarproductos(request, id):
    producto=get_object_or_404(Producto,id=id)
    producto.delete()
    return redirect(to="listaproductos")
@permission_required('change_soporte')
def crearproductos(request):
    form=frmProducto(request.POST or None)
    contexto={
        "form":form
    }
    
    if request.method=="POST":
        form=frmProducto(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect(to="listaproductos")
    
    return render(request,"app/crearproductos.html",contexto)

#modificar estado envio
@permission_required('change_soporte')
def listapedidosadm(request):
    listaen=Pedido.objects.all()
    contexto={
        "pedidos":listaen
    }
    return render(request,"app/modenvios.html",contexto)
@permission_required('change_soporte')
def modificarpedidos(request,id):
    pedido=get_object_or_404(Pedido,id=id)
    
    form=frmEnvio(instance=pedido)
  
    contexto={
        "form":form
    }
    
    if request.method=="POST":
        form=frmEnvio(data=request.POST,instance=pedido)
        
        if form.is_valid():
            datos=form.cleaned_data
            pedi=Pedido.objects.get(id=id)
            pedi.estado=datos.get("Estado")
            pedi.save()
            return redirect(to="modenvios")
      
            
    return render(request,"app/modificarestado.html",contexto)

#soporte
def soporte(request):
    data = {
        'form': SoporteForm()
    }

    if request.method == "POST":
        formulario = SoporteForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "MENSAJE ENVIADO"
            return redirect(to="index")
        else:         
            data["form"] = formulario

    return render(request, 'app/soporte.html', data)
@permission_required('change_soporte')
def listadosoporte(request):
    listado=Soporte.objects.all()
    contexto={
        "soporte":listado
    }
    return render(request,"app/listadosoporte.html",contexto)
@permission_required('change_soporte')
def eliminarsoporte(request, id):
    soporte=get_object_or_404(Soporte,id=id)
    soporte.delete()
    return redirect(to="listadosoporte")

# pruebas carrito
@login_required()
def cart_add(request, id, precio):
    carrito= Carrito()
    producto = Producto.objects.get(id=id)
    carrito.idusuario=request.user.username
    carrito.idprod=id
    carrito.nomproduc=producto
    carrito.candtidad=1
    carrito.precio= precio
    carrito.save()


    

    return redirect(to="carrito")
    
@login_required()
def cantidad(request):
    form=frmCantidad(request.POST or None)
    contexto={
        "form":form
    }
    
    if request.method=="POST":
        form=frmCantidad(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="index")
    
    return render(request,"app/perro.html",contexto)  
@login_required()
def comprar(request,id):
    pedido= Pedido()
    pedido.nomusuario=request.user.username
    pedido.fecha=datetime.now()
    pedido.estado=1
    pedido.direccion="laraquete 900"
    pedido.save()

    carrito=get_object_or_404(Carrito,id=id)
    carrito.delete()
    return redirect(to="perfil")
@permission_required('change_soporte')
def datoseg(request,id):
    pedido=get_object_or_404(Pedido,id=id)
    detalle= Detalle()
    detalle.producto= Producto.objects.get(id=id)
    detalle.valor= 1000
    detalle.cantidad= 1
    detalle.pedido= pedido
    detalle.save()
    return redirect(to="index")

@login_required()
def seguimiento(request):
    return render(request,"app/seguimiento.html")