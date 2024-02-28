from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('comic', comic, name="comic"),
    path('cliente', cliente, name="cliente"),
    path('distribuidor', distribuidor, name="distribuidor"),
    path('envio', envio, name="envio"),
    
    
# RUTAS DE FORM ___________________________________________________
    path('clienteForm', clienteForm, name="clienteForm"),
    path('comicForm', comicForm, name="comicForm"),
    path('distribuidorForm', distribuidorForm, name="distribuidorForm"),
    path('envioForm', envioForm, name="envioForm"),
    
    
# RUTAS DE BUSCAR COMIC ___________________________________________________
    path('buscar/', buscar, name="buscar"),
    path('buscarComic/', buscarComic, name="buscarComic"),
    

# RUTAS DE MODIFICAR ___________________________________________________
    path('modificar_cliente/<id_cliente>/', modificarCliente, name="modificarCliente"),
    path('modificar_comic/<id_comic>/', modificarComic, name="modificarComic"),
    path('modificar_distribuidor/<id_distribuidor>/', modificarDistribuidor, name="modificarDistribuidor"),
    path('modificar_envio/<id_envio>/', modificarEnvio, name="modificarEnvio"),


# RUTAS DE BORRAR ___________________________________________________
    path('borrar_cliente/<id_cliente>/', borrarCliente, name="borrarCliente"),
    path('borrar_comic/<id_comic>/', borrarComic, name="borrarComic"),
    path('borrar_distribuidor/<id_distribuidor>/', borrarDistribuidor, name="borrarDistribuidor"),
    path('borrar_envio/<id_envio>/', borrarEnvio, name="borrarEnvio"),

]
