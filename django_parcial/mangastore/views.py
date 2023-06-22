from django.shortcuts import render, redirect
from .forms import CustomUserForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, authenticate

# Create your views here.

def home(request):
    return render(request, 'mangastore/home.html')

def colecciones(request):
    return render(request, 'mangastore/colecciones.html')

def quisomos(request):
    return render(request, 'mangastore/quisomos.html')

def contacto(request):
    return render(request, 'mangastore/contacto.html')
@login_required
def carr(request):
    return render(request, 'mangastore/carr.html')

def registro_usuario(request):
    data = {
        'form':CustomUserForm()
    }
    if request.method == 'POST':
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid:
            formulario.save();
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(to='home')
    return render(request, "registration/registrar.html", data)