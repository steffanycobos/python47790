from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from AppCoder.models import Familia

# Create your views here.
def inicio_view(xx):
    user= Familia(nombre='jesus',apellido='Cobos', fecha='1994-12-17')
    #user.save()
    mihtml=open(r'proyectoFinal\AppCoder\templates\padre.html')
    html_read= Template(mihtml.read())
    mihtml.close()
    miContexto= Context(user)
    documento=html_read.render(miContexto)
    return HttpResponse(documento)


def probandoTemplate(xx):
    user= Familia(nombre='Leandra',apellido='Cobos', fecha='1994-12-17')
    nombre=user.nombre
    apellido= user.apellido
    usuario={'nombre':nombre, 'apellido':apellido}
    print(user)
    mihtml=open(r'proyectoFinal\AppCoder\templates\padre.html')
    html_read= Template(mihtml.read())
    mihtml.close()
    miContexto= Context(usuario)
    documento=html_read.render(miContexto)
    return HttpResponse(documento)
 
