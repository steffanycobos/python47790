from django.urls import path
from django.http import HttpResponse
from AppCoder.views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
   
    path("", inicio_view),
    path("newproduct/", createProducts),
    path('newuser', creatUser, name='newUser'),
    path('buscar', findUser),
    path('usuarioEncontrado',UsuarioEncontrado, name='UsuarioEncontrado'),
    path('products', allProduct, name='allProducts'),
    path('user',showUser,name='showUser'),
    path('detailProduct',index, name='index'),
    path('login', login_view, name='login'),
    path('logout', LogoutView.as_view(template_name="index.html")),
    path('delete/<product_id>',products_delete, name='products_delete')
    
]
print('ok!')
