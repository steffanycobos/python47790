from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, UserModel
from . import models

class UserCreationFormulario(UserCreationForm):
     email = forms.EmailField()
     password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
     password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
     avatar= forms.ImageField(label='Imagen',widget=forms.FileInput)

     class Meta:
        model = UserModel
        fields = ["username", "email","password1", "password2",'avatar' ]
        help_texts = {k: "" for k in fields}
      
class UserEditionFormulario(UserChangeForm):
    email = forms.EmailField()
    first_name = forms.CharField(label="Nombre", widget=forms.PasswordInput)
    last_name = forms.CharField(label="Apellido", widget=forms.PasswordInput)
    password = None

    class Meta:
        model = UserModel
        fields = ["email", "first_name", "last_name"]
        help_texts = {k: "" for k in fields}

        

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
    
    