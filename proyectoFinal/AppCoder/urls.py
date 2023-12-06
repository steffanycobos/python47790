from django.urls import path
from django.http import HttpResponse
from AppCoder.views import *


urlpatterns = [
   
    path("", inicio_view),
    path("newproduct/", createProducts),
    path('newuser', creatUser, name='newUser'),
    path('buscar', findUser),
    path('usuarioEncontrado',UsuarioEncontrado, name='UsuarioEncontrado'),
    path('products', allProduct, name='allProducts'),
    path('user',showUser,name='showUser'),
    path('detailProduct',index, name='index')
    
]
print('ok!')
