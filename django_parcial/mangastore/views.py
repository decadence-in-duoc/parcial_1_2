from django.shortcuts import render, redirect
from .forms import CustomUserForm, MangaForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, authenticate
from .models import Producto
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'mangastore/home.html')

def colecciones(request):
    products = Producto.objects.all()
    data = {
        'products':products
    }
    return render(request, 'mangastore/colecciones.html', data)

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
            messages.success(request, "Registro completado")
            return redirect(to='home')
    return render(request, "registration/registrar.html", data)


# productos

def product_list(request):
    mangas = Producto.objects.all()
    data = {
        'mangas':mangas
    }
    return render(request, 'mangastore/listprod.html', data)

def add_product(request):
    data = {
        'form': MangaForm()
    }
    
    if request.method == 'POST':
        formulario = MangaForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Guardado correctamente"
            messages.success(request, "Producto agregado")
            return redirect(to='product_list')
    return render(request, 'mangastore/addprod.html', data)

def mod_product(request, id):
    mangas = Producto.objects.get(id=id)
    data = {
        'form':MangaForm(instance=mangas)
    }
    if request.method == 'POST':
        formulario = MangaForm(data = request.POST, instance = mangas, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Modificado correctamente"
            data['form'] = formulario
            messages.success(request, "Producto modificado")
            return redirect(to='product_list')
    return render(request, 'mangastore/modprod.html', data)

def del_prod(request, id):
    mangas = Producto.objects.get(id=id)
    mangas.delete()
    messages.success(request, "Producto eliminado")
    return redirect(to="product_list")
