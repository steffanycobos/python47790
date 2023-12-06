from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, Context
from AppCoder.models import *
from . import forms



# Create your views here.
def inicio_view(xx):   ##INDEX
    mihtml=open(r'proyectoFinal\AppCoder\templates\index.html')
    html_read= Template(mihtml.read())
    mihtml.close()
    miContexto= Context(html_read)
    documento=html_read.render(miContexto)
    return HttpResponse(documento)



def creatUser(request):  #CREA UN USUARIO
    if request.method == "POST":
        form = forms.UserForm(request.POST)
        if form.is_valid():
            #form.save()
            return redirect('/AppCoder/user')
    else:
        form = forms.UserForm()
    return render(request, "formUser.html", {"form": form})


def createProducts(request):  ##CREA UN PRODUCTO
    if request.method == "POST":
        form = forms.ProductsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Validado')
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
        return HttpResponse('Envia datos pararegistrar la solicitud.')


def allProduct(request):   ## MUESTRA TODOS LOS PRODUCTOS
    products= Products.objects.all()
    return render(request,'allProducts.html', {'products':products})

def showUser(request):  # MUESTRA AL USUARIO LUEGO DE REGISTRARSE
    users = Users.objects.all()
    lusers = list(users) 
    last = lusers[-1]
    return render(request,'showUser.html', {'user':last})

def index(request):  #FALLA BARRA DE BUSQUEDA
    queryset =request.GET.get("search")
    if queryset:  
        products= Products.objects.filter(title__icontains=queryset)  # sirve para buscar el distinct sirve para traer los distintos post
    return redirect(request, "/AppCoder/detailProduct", {'products':products})
