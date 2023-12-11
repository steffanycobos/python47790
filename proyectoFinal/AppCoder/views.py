from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import auth
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from AppCoder.models import *
from . import forms
from .forms import ProductsForm, UserCreationFormulario, UserEditionFormulario



# Create your views here.
def inicio_view(request):   ##INDEX
    return render(request,'index.html')


def creatUser(request):  #CREA UN USUARIO
       if request.method == "GET":
        return render(
            request,
            "formUser.html",
            {"form": UserCreationFormulario()}
        )
       else:
        formulario = UserCreationFormulario(request.POST,request.FILES)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            usuario = informacion["username"]
            formulario.save()

            return render(
                request,
                "index.html",
                {"mensaje": f"Usuario creado: {usuario}"}
            )
        else:
            return render(
                request,
                "formUser.html",
                {"form": formulario}
            )

def login_view(request):
    if request.user.is_authenticated:
        print('ya esta')
        return render(
            request,
            "index.html",
            {"mensaje": f"Ya estás autenticado: {request.user.username}"}
        )

    if request.method == "GET":
        return render(
            request,
            "login.html",
            {"form": AuthenticationForm()}
        )
    else:
        formulario = AuthenticationForm(request, data=request.POST)

        if formulario.is_valid():
            informacion = formulario.cleaned_data
            usuario = informacion["username"]
            password = informacion["password"]

            modelo = authenticate(username=usuario, password=password)
            login(request, modelo)

            return render(
                request,
                "index.html",
                {"mensaje": f"Bienvenido {modelo.username}"}
            )
        else:
            return render(
                request,
                "login.html",
                {"form": formulario}
            )

        
def createProducts(request):  ##CREA UN PRODUCTO
    if request.method == "POST":
        form = forms.ProductsForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Producto creado con éxito!')
    else:
        form = forms.ProductsForm()
    return render(request, "formProducts.html", {"form": form})

def allProduct(request):   ## MUESTRA TODOS LOS PRODUCTOS
    products= Products.objects.all()
    return render(request,'allProducts.html', {'products':products}) 


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

def products_delete(request, product_id):
    product_delete= Products.objects.filter(id=product_id).first()
    product_delete.delete()
    return allProduct(request)