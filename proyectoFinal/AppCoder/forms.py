from django import forms

from . import models


class UserForm(forms.ModelForm):
    class Meta:
        model = models.Users
        fields = ["nombre", "apellido", "email", "password"]
    


class ProductsForm(forms.ModelForm):
    class Meta:
        model = models.Products
        fields = ["title", "description", "price", "stock","imagen"]
    