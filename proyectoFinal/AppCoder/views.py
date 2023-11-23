from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context

# Create your views here.
def inicio_view(xx):
    return HttpResponse("Bienvenidos!!!!!!!!!!!!!!")

def probandoTemplate(xx):
    mihtml=open(r'C:\Users\Steffany Cobos\Desktop\python_proyecto\proyectoFinal\AppCoder\templates\padre.html')
    html_read= Template(mihtml.read())

    mihtml.close()
    miContexto= Context()
    documento=html_read.render(miContexto)
    return HttpResponse(documento)
 
