from django.urls import path
from django.http import HttpResponse
from AppCoder.views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
   
    path("", inicio_view, name='inicio'),
    path('products', allProduct, name='allProducts'),
    path("newproduct/", createProducts),
    path('editarProducto/<product_id>', editProduct, name='editProduct'),
    path('productSearch',index, name='index'),
    path('detailProduct/<product_id>',detailProduct, name='detailProduct'),
    path('delete/<product_id>',products_delete, name='products_delete'),
    path('newuser', creatUser, name='newUser'),
    path('login', login_view, name='login'),
    path('editarPerfil', editUser, name='editUser'),
    path('profile',profile,name= 'profile'),
    path('logout', LogoutView.as_view(template_name="index.html")),
    path('aboutme',aboutme, name='aboutme')

    
]

