from django.urls import include, path

from app.views import preparacion,encamino,entregado,eliminarsoporte,listadosoporte,soporte,modificarpedidos,listapedidosadm,datoseg,seguimiento,comprar,eliminarproductocarrito,cambiarpassword,registro,perfilusuario,crearperfil,index,perro,roedor,gatos,aves,anfibios,quienes,listado,crear,modificar,eliminar,perfil,listaproductos,modificarproductos,eliminarproductos,crearproductos,cart_add,cantidad,carrito

urlpatterns = [
    path('', index, name='index'),
    path('roedor', roedor, name='roedor'),
    path('perro', perro, name='perro'),
    path('gatos', gatos, name='gatos'),
    path('aves', aves, name='aves'),
    path('anfibios', anfibios, name='anfibios'),
    path('quienes', quienes, name='quienes'),
    path('listado/',listado,name="listado"),
    path('crear/',crear,name="crear"),
    path('modificar/<id>',modificar,name="modificar"),
    path('eliminar/<id>',eliminar,name="eliminar"),
    path('cambiarpassword/',cambiarpassword,name="cambiarpassword"),
    path('registro/',registro,name="registro"),
    path('perfilusuario/',perfilusuario,name="perfilusuario"),
    path('perfil/',perfil,name="perfil"),
    path('listaproductos/',listaproductos,name="listaproductos"),
    path('modificarproductos/<id>',modificarproductos,name="modificarproductos"),
    path('eliminarproductos/<id>',eliminarproductos,name="eliminarproductos"),
    path('crearproductos/',crearproductos,name="crearproductos"),

    path('cart_add/<id>/<precio>', cart_add, name='cart_add'),
    path('cantidad',cantidad,name='cantidad'),
    path('carrito',carrito,name='carrito'),
    path('eliminarproductocarrito/<id>',eliminarproductocarrito,name='eliminarproductocarrito'),
    path('comprar/<id>/',comprar,name='comprar'),
    path('seguimiento/<id>',seguimiento,name='seguimiento'),
    path('datoseg/<id>/',datoseg,name='datoseg'),
    path('listapedidosadm',listapedidosadm,name='listapedidosadm'),
    path('modificarpedidos/<id>/',modificarpedidos,name='modificarpedidos'),
    path('soporte', soporte, name="soporte"),
    path('listadosoporte', listadosoporte, name="listadosoporte"),
    path('eliminarsoporte/<id>',eliminarsoporte,name="eliminarsoporte"),

    path('preparacion',preparacion,name="preparacion"),
    path('encamino',encamino,name="encamino"),
    path('entregado',entregado,name="entregado"),
    

    path('crearperfil',crearperfil,name="crearperfil")
    
]
