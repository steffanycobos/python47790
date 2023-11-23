from django.urls import path
from django.http import HttpResponse
from AppCoder.views import probandoTemplate, inicio_view


urlpatterns = [
    path("prueba/", probandoTemplate),
    path("inicio/", inicio_view),
]
print('ok!')
