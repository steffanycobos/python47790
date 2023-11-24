from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from AppCoder.models import Familia

# Create your views here.
def inicio_view(self):
    user= Familia(nombre='Leandra',apellido='Cobos', fecha='1994-12-17')
    user.save()
    userTexto= f'Nombre: {user.nombre}, Apellido: {user.apellido}, Nacimiento: {user.fecha}'
    return HttpResponse(userTexto)

def probandoTemplate(xx):
    mihtml=open(r'C:\Users\Steffany Cobos\Desktop\python_proyecto\proyectoFinal\AppCoder\templates\padre.html')
    html_read= Template(mihtml.read())

    mihtml.close()
    miContexto= Context()
    documento=html_read.render(miContexto)
    return HttpResponse(documento)
 
