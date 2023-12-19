from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, User
from . import models

class UserCreationFormulario(UserCreationForm):
     email = forms.EmailField()
     password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
     password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
     
     

     class Meta:
        model = User
        fields = ["username", "email","password1", "password2"]
        help_texts = {k: "" for k in fields}
      
class UserEditionFormulario(UserCreationForm):
    username=forms.CharField(label= 'Username')
    email = forms.EmailField(label="Ingrese su email:")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ['username','email','password1','password2']
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
            'imagen': forms.FileInput(attrs={'class':'form-control', 'id':'formFile'}),
            
        }
    
class ProductEditionFormulario(forms.ModelForm):
    title=forms.CharField(label='Nombre', widget=forms.TextInput)
    description=forms.CharField(label='Descripción', widget=forms.TextInput)
    price= forms.FloatField(label='Precio',widget= forms.NumberInput)
    stock= forms.IntegerField(label='Stock',widget=forms.NumberInput)
    imagen=forms.FileField(label='Imagen',widget= forms.FileInput)
    

    class Meta:
        model = models.Products
        fields = ['title','description','price','stock','imagen']
        help_texts = {k: "" for k in fields}


class AvatarForm(forms.ModelForm):
    avatar= forms.FileField(label='Avatar', widget=forms.FileInput)

    class Meta:
        model = models.Avatar
        fields = ['avatar']
        help_texts = {k: "" for k in fields}
