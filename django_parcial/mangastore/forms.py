from django import forms
from django.forms import ModelForm
from django.forms import fields
from .models import Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# class MangaForm(ModelForm):

class CustomUserForm(UserCreationForm):
    pass
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']
        

# clase para añadir productos

class MangaForm(ModelForm):
    
    nombre = forms.CharField(min_length=3, max_length=100)
    precio = forms.IntegerField(min_value=1, max_value=1500000)
    image = forms.ImageField(required=False)
    
    class Meta:
        model = Producto
        fields = ['nombre', 'categoria', 'descripcion', 'precio', 'image']