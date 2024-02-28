from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy

from .models import *
from .forms import *


##_______________________________________________ HOME _________________________________________________________________________________________________
def home(request):
    return render(request, "comiqueriapp/home.html")


##__________________________ CLIENTE __________________________________________________________________________________________________________________

def cliente(request):
    contexto = {'cliente': Cliente.objects.all()}
    return render(request, "comiqueriapp/cliente.html", contexto)


def clienteForm(request):
    if request.method == "POST":
        miForm = ClienteForm(request.POST)
        if miForm.is_valid():
            cliente_apellido = miForm.cleaned_data.get("apellido")
            cliente_nombre = miForm.cleaned_data.get("nombre")
            cliente_telefono = miForm.cleaned_data.get("telefono")
            cliente = Cliente(apellido=cliente_apellido, nombre=cliente_nombre, telefono=cliente_telefono)
            cliente.save()
            return redirect(reverse_lazy('cliente'))
    else:
        miForm = ClienteForm()

    return render(request, "comiqueriapp/clienteForm.html", {"form": miForm})


def modificarCliente(request, id_cliente):
    cliente= Cliente.objects.get(id=id_cliente)
    if request.method == "POST":
        miForm = ClienteForm(request.POST)
        if miForm.is_valid():
            cliente.apellido = miForm.cleaned_data.get("apellido")
            cliente.nombre = miForm.cleaned_data.get("nombre")
            cliente.telefono = miForm.cleaned_data.get("telefono")
            cliente = Cliente(apellido=cliente.apellido, nombre=cliente.nombre, telefono=cliente.telefono)
            cliente.save()
            return redirect(reverse_lazy('cliente'))
    else:
        miForm = ClienteForm(initial={
            'apellido': cliente.apellido,
            'nombre': cliente.nombre,
            'telefono': cliente.telefono,
        })
        return render(request, "comiqueriapp/clienteForm.html", {"form": miForm})
    
    
def borrarCliente(request, id_cliente):
        cliente = Cliente.objects.get(id=id_cliente)
        cliente.delete()
        return redirect(reverse_lazy('cliente'))
    
    
##__________________________ COMICS __________________________________________________________________________________________________________________

def comic(request):
    contexto = {'comic': Comic.objects.all()}
    return render(request, "comiqueriapp/comic.html", contexto)


def comicForm(request):
    if request.method == "POST":
        miForm = ComicForm(request.POST)
        if miForm.is_valid():
            comic_nombre = miForm.cleaned_data.get("nombre")
            comic_editorial = miForm.cleaned_data.get("editorial")
            comic_autor = miForm.cleaned_data.get("autor")
            comic = Comic(nombre=comic_nombre, editorial=comic_editorial, autor=comic_autor)
            comic.save()
            return redirect(reverse_lazy('comic'))
    else:
        miForm = ComicForm()

    return render(request, "comiqueriapp/comicForm.html", {"form": miForm})

def modificarComic(request, id_comic):
    comic= Comic.objects.get(id=id_comic)
    if request.method == "POST":
        miForm = ComicForm(request.POST)
        if miForm.is_valid():
            comic.nombre = miForm.cleaned_data.get("nombre")
            comic.editorial = miForm.cleaned_data.get("editorial")
            comic.autor = miForm.cleaned_data.get("autor")
            comic = Comic(nombre=comic.nombre, editorial=comic.editorial, autor=comic.autor)
            comic.save()
            return redirect(reverse_lazy('comic'))
    else:
        miForm = ComicForm(initial={
            'nombre': comic.nombre,
            'editorial': comic.editorial,
            'autor': comic.autor,
        })
        return render(request, "comiqueriapp/comicForm.html", {"form": miForm})
    
    
def borrarComic(request, id_comic):
        comic = Comic.objects.get(id=id_comic)
        comic.delete()
        return redirect(reverse_lazy('comic'))
    

##__________________________ DISTRIBUIDORES __________________________________________________________________________________________________________________

def distribuidor(request):
    contexto = {'distribuidor': Distribuidor.objects.all()}
    return render(request, "comiqueriapp/distribuidor.html", contexto)


def distribuidorForm(request):
    if request.method == "POST":
        miForm = DistribuidorForm(request.POST)
        if miForm.is_valid():
            distribuidor_nombre = miForm.cleaned_data.get("nombre")
            distribuidor_direccion = miForm.cleaned_data.get("direccion")
            distribuidor_telefono = miForm.cleaned_data.get("telefono")
            distribuidor = Distribuidor(nombre=distribuidor_nombre, direccion=distribuidor_direccion, telefono=distribuidor_telefono)
            distribuidor.save()
            return redirect(reverse_lazy('distribuidor'))
    else:
        miForm = DistribuidorForm()

    return render(request, "comiqueriapp/distribuidorForm.html", {"form": miForm})


def modificarDistribuidor(request, id_distribuidor):
    distribuidor= Distribuidor.objects.get(id=id_distribuidor)
    if request.method == "POST":
        miForm = DistribuidorForm(request.POST)
        if miForm.is_valid():
            distribuidor.nombre = miForm.cleaned_data.get("nombre")
            distribuidor.direccion = miForm.cleaned_data.get("direccion")
            distribuidor.telefono = miForm.cleaned_data.get("telefono")
            distribuidor = Distribuidor(nombre=distribuidor.nombre, direccion=distribuidor.direccion, telefono=distribuidor.telefono)
            distribuidor.save()
            return redirect(reverse_lazy('distribuidor'))
    else:
        miForm = DistribuidorForm(initial={
            'nombre': distribuidor.nombre,
            'direccion': distribuidor.direccion,
            'telefono': distribuidor.telefono,
        })
        return render(request, "comiqueriapp/distribuidorForm.html", {"form": miForm})
    
    
def borrarDistribuidor(request, id_distribuidor):
        distribuidor = Distribuidor.objects.get(id=id_distribuidor)
        distribuidor.delete()
        return redirect(reverse_lazy('distribuidor'))
    
    
##__________________________ ENVÍOS __________________________________________________________________________________________________________________

def envio(request):
    contexto = {'envio': Envio.objects.all()}
    return render(request, "comiqueriapp/envio.html", contexto)


def envioForm(request):
    if request.method == "POST":
        miForm = EnvioForm(request.POST)
        if miForm.is_valid():
            envio_empresa = miForm.cleaned_data.get("empresa")
            envio_nombre= miForm.cleaned_data.get("nombre")
            envio_telefono = miForm.cleaned_data.get("telefono")
            envio = Envio(empresa=envio_empresa, nombre=envio_nombre, telefono=envio_telefono)
            envio.save()
            return redirect(reverse_lazy('envio'))
    else:
        miForm = EnvioForm()

    return render(request, "comiqueriapp/envioForm.html", {"form": miForm})
    
    
def modificarEnvio(request, id_envio):
    envio= Envio.objects.get(id=id_envio)
    if request.method == "POST":
        miForm = EnvioForm(request.POST)
        if miForm.is_valid():
            envio.empresa = miForm.cleaned_data.get("empresa")
            envio.nombre = miForm.cleaned_data.get("nombre")
            envio.telefono = miForm.cleaned_data.get("telefono")
            envio = Envio(empresa=envio.empresa, nombre=envio.nombre, telefono=envio.telefono)
            envio.save()
            return redirect(reverse_lazy('envio'))
    else:
        miForm = EnvioForm(initial={
            'empresa': envio.empresa,
            'nombre': envio.nombre,
            'telefono': envio.telefono,
        })
        return render(request, "comiqueriapp/envioForm.html", {"form": miForm})
    
    
def borrarEnvio(request, id_envio):
        envio = Envio.objects.get(id=id_envio)
        envio.delete()
        return redirect(reverse_lazy('envio'))


##__________________________ BUSCAR UN COMIC __________________________________________________________________________________________________________________

def buscar(request):
    return render(request, "comiqueriapp/buscar.html")

def buscarComic(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        comic = Comic.objects.filter(nombre__icontains=patron)
        contexto = {"comic": comic}
        return render(request, "comiqueriapp/comic.html", contexto)
    return HttpResponse("No se ingresaron patrones de busqueda")