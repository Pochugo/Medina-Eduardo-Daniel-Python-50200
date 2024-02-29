from django.urls import path, include
from .views import *

from django.urls import path
from .views import login_request

from django.contrib.auth.views import LogoutView

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

# LOGIN, LOGOUT, REGISTRACIÓN, EDITAR PERFIL ___________________________________________________
    path('login/', login_request, name="login"),
    path('registro/', register, name="registro"),
    path('logout/', custom_logout, name='logout'),
    path('editar_perfil/', editarPerfil, name="editar_perfil"),
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar"),

]
