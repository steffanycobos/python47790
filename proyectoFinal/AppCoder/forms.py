from django import forms

from . import models


class UserForm(forms.ModelForm):
    class Meta:
        model = models.Users
        fields = ["nombre", "apellido", "email", "password"]
        widgets={
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellido': forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'})
        }
    


class ProductsForm(forms.ModelForm):
    class Meta:
        model = models.Products
        fields = ["title", "description", "price", "stock","imagen"]
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.TextInput(attrs={'class':'form-control'}),
            'price':forms.NumberInput(attrs={'class':'form-control'}),
            'stock':forms.NumberInput(attrs={'class':'form-control'}),
            'imagen': forms.FileInput(attrs={'class':'form-control', 'id':'formFile'})
    
        }
    