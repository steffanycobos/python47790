from django.urls import path
from django.http import HttpResponse
from AppCoder.views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
   
    path("", inicio_view),
    path("newproduct/", createProducts),
    path('newuser', creatUser, name='newUser'),
    path('editarPerfil', editUser, name='editUser'),
    path('editarProducto/<product_id>', editProduct, name='editProduct'),
    path('products', allProduct, name='allProducts'),
    path('productSearch',index, name='index'),
    path('login', login_view, name='login'),
    path('logout', LogoutView.as_view(template_name="index.html")),
    path('delete/<product_id>',products_delete, name='products_delete'),
    path('profile/',profile,name= 'profile'),
    path('detailProduct/<product_id>',detailProduct, name='detailProduct'),
    path('aboutme',aboutme, name='aboutme')

    
]

