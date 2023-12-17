from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import auth
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from AppCoder.models import *
from .forms import UserCreationFormulario, UserEditionFormulario, ProductEditionFormulario, AvatarForm
from . import forms



# Create your views here.
def inicio_view(request):   ##INDEX
    return render(request,'index.html')


def creatUser(request):  #CREA UN USUARIO
       if request.method == "GET":
        return render(request, "formUser.html", {"form": UserCreationFormulario()})
       else:
        formulario = UserCreationFormulario(request.POST,request.FILES)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            usuario = informacion["username"]
            messages.success(request,'Usuario creado con éxito!')
            formulario.save()
            return render(request,"index.html" )
       
        else:
            return render(  request,   "formUser.html",  {"form": formulario} )
        
def profile(request): ##PERFIL DEL USURIO
    if request.method=='POST':
        form= AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            usuario=User.objects.get(username=request.user)
            avatar= Avatar(user=usuario, imagen=form.cleaned_data['avatar'])
            avatar.save()
            return render(request,'index.html')
        else:
            return HttpResponse(form.errors)
    else:
        usuario=request.user
        avatares=Avatar.objects.filter(user=request.user.id)
        form=AvatarForm()
        return render(request,'profile.html',{'form':form, 'user':usuario, 'url':avatares[0].imagen.url})




def editUser(request): ##EDITAR USUARIO
    usuario=request.user
    if (request.method=='POST'):
        form= UserEditionFormulario(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            usuario.username=info['username']
            usuario.email=info['email']
            usuario.password1=info['password1']
            usuario.password1=info['password2']
            usuario.save()
            return HttpResponse('Usuario editado con éxito')
    else:
        form= UserEditionFormulario(initial={'email':usuario.email})
        return render(request, 'editUser.html', {'form':form, 'usuario':usuario})

def login_view(request): ##LOGIN DE USUARIO
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
                "index.html")
            
        else:
            return render(
                request,
                "login.html",
                {"form": formulario}
            )




def createProducts(request):  ##CREA UN PRODUCTO
    form = forms.ProductsForm(request.POST,request.FILES)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return render(request, 'allProducts.html')
    else:
        form = forms.ProductsForm()
        messages.success(request,'Producto creado con éxito!')
    return render(request, "formProducts.html", {"form": form})


def editProduct(request, product_id): #EDITAR PRODUCTO
    product=Products.objects.filter(id=product_id).first()
    if request.method=='POST':
        formulario= ProductEditionFormulario(request.POST, request.FILES)
        if formulario.is_valid():
            info= formulario.cleaned_data
            product.title= info['title']
            product.description= info['description']
            product.price=info['price']
            product.stock=info['stock']
            product.imagen=info['imagen']
            product.save()

            return render(request, 'allProducts.htmls')
        else:
            return HttpResponse(formulario.errors)
        
    else:
        formulario= ProductEditionFormulario(initial={'title':product.title, 'description':product.description, 'price':product.price,'stock':product.stock, 'imagen':product.imagen})
        return render(request, 'editProduct.html',{'form':formulario, 'id':product.id})
   

def allProduct(request):   ## MUESTRA TODOS LOS PRODUCTOS
    products= Products.objects.all()
    return render(request,'allProducts.html', {'products':products}) 

def detailProduct(request, product_id): #DETALLE DE PRODUCTO
    product=Products.objects.filter(id=product_id).first()
    return render(request, 'detailProduct.html',{'product':product})


def index(request):  #BARRA DE BUSQUEDA
   if ( "search" in request.GET):
        filtro = request.GET["search"]
        products = Products.objects.filter(title__icontains=filtro)
        return render( request, "productSearch.html", {'products':products}  )
   else:
        return HttpResponse('Envia datos para registrar la solicitud.')

def products_delete(request, product_id): ## ELIMINAR PRODUCTO
    product_delete= Products.objects.filter(id=product_id).first()
    product_delete.delete()
    return allProduct(request)

def aboutme(request): 
    return render(request,'aboutme.html')