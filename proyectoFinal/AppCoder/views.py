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
from tkinter import messagebox


# Create your views here.

def inicio_view(request):   ##INDEX
      if request.user.is_authenticated:
        usuario = request.user
        avatar = Avatar.objects.filter(user=usuario).first()
        avatar_url = avatar.imagen.url if avatar is not None else ""
      else:
       avatar_url = ""

      return render(request, "index.html",context= {'avatar_url':avatar_url})



def creatUser(request):  #CREA UN USUARIO
       if request.method == "GET":
        return render(request, "formUser.html", {"form": UserCreationFormulario()})
       else:
        formulario = UserCreationFormulario(request.POST,request.FILES)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            usuario = informacion["username"]
            formulario.save()
            return redirect ("/AppCoder/profile")
       
        else:
            return render(  request,   "formUser.html",  {"form": formulario} )
@login_required 
def profile(request): ##PERFIL DEL USURIO
    usuario = request.user

    if request.method == "GET":
        formulario = AvatarForm()
        return render(
            request,
            "profile.html",
            context={"form": formulario, "usuario": usuario}
        )
    else:
        formulario = AvatarForm(request.POST, request.FILES)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            modelo = Avatar(user=usuario, imagen=informacion["avatar"])
            modelo.save()
            
            return redirect("/AppCoder")



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
            return redirect('/AppCoder/profile')
        else:
            return HttpResponse(f' Error en: {form.errors}')
    else:
        form= UserEditionFormulario(initial={'email':usuario.email})
        return render(request, 'editUser.html', {'form':form, 'usuario':usuario})

def login_view(request): ##LOGIN DE USUARIO
    if request.user.is_authenticated:
       
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
            messages.success(request,'Producto creado con éxito!')
            return redirect('/AppCoder/products')
    else:
        form = forms.ProductsForm()
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

            return render(request, 'allProducts.html')
        else:
            return HttpResponse(formulario.errors)
        
    else:
        formulario= ProductEditionFormulario(initial={'title':product.title, 'description':product.description, 'price':product.price,'stock':product.stock, 'imagen':product.imagen})
        return render(request, 'editProduct.html',{'form':formulario, 'id':product.id})
   

def allProduct(request):   ## MUESTRA TODOS LOS PRODUCTOS
    products= Products.objects.all()
    if request.user.is_authenticated:
        usuario = request.user
        avatar = Avatar.objects.filter(user=usuario).first()
        avatar_url = avatar.imagen.url if avatar is not None else ""
     
    else:
       avatar_url = ""

    return render(request,'allProducts.html', {'products':products,"avatar_url": avatar_url}) 

def detailProduct(request, product_id): #DETALLE DE PRODUCTO
    product=Products.objects.filter(id=product_id).first()
    usuario=request.user
    if request.user.is_authenticated:
        usuario = request.user
        avatar = Avatar.objects.filter(user=usuario).first()
        avatar_url = avatar.imagen.url if avatar is not None else ""
    else:
       avatar_url = ""
    return render(request, 'detailProduct.html',{'product':product,'avatar_url':avatar_url})


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
    usuario=request.user
    if request.user.is_authenticated:
        usuario = request.user
        avatar = Avatar.objects.filter(user=usuario).first()
        avatar_url = avatar.imagen.url if avatar is not None else ""
    else:
       avatar_url = ""
    return render(request,'aboutme.html', {'avatar_url':avatar_url})