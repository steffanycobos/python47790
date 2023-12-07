from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, Context
from AppCoder.models import *
from . import forms



# Create your views here.
def inicio_view(request):   ##INDEX
    return render(request,'index.html')



def creatUser(request):  #CREA UN USUARIO
    if request.method == "POST":
        form = forms.UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/AppCoder/user')
    else:
        form = forms.UserForm()
    return render(request, "formUser.html", {"form": form})


def createProducts(request):  ##CREA UN PRODUCTO
    if request.method == "POST":
        form = forms.ProductsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Producto creado con éxito!')
    else:
        form = forms.ProductsForm()
    return render(request, "formProducts.html", {"form": form})


def findUser(request):  
    return render(request, "findUser.html")

def UsuarioEncontrado(request):  ##MUESTRA LOS USUARIOS ENCONTRADOS
    if ( "user" in request.GET):
        filtro = request.GET["user"]
        print(filtro)
        usuario = Users.objects.filter(nombre__icontains=filtro)
        return render( request, "usuario.html", {"usuario": usuario}  )
    else:
        return HttpResponse('Envia datos para registrar la solicitud.')


def allProduct(request):   ## MUESTRA TODOS LOS PRODUCTOS
    products= Products.objects.all()
    return render(request,'allProducts.html', {'products':products})

def showUser(request):  # MUESTRA AL USUARIO LUEGO DE REGISTRARSE
    users = Users.objects.all()
    lusers = list(users) 
    last = lusers[-1]
    return render(request,'showUser.html', {'user':last})

def index(request):  #BARRA DE BUSQUEDA
   if ( "search" in request.GET):
        filtro = request.GET["search"]
        products = Products.objects.filter(title__icontains=filtro)
        return render( request, "detailProduct.html", {'products':products}  )
   else:
        return HttpResponse('Envia datos para registrar la solicitud.')
