from django.shortcuts import redirect, render
from .models import Producto
from .forms import ProductoForm


# Create your views here.

def home(request):
    return render(request, 'mangastore/home.html')

def colecciones(request):
    return render(request, 'mangastore/colecciones.html')

def quisomos(request):
    return render(request, 'mangastore/quisomos.html')

def contacto(request):
    return render(request, 'mangastore/contacto.html')

def carr(request):
    return render(request, 'mangastore/carr.html')

def lista_manga(request):
    producto = Producto.objects.all()
    context = {"producto":producto}
    return render(request,'mangastore/lista_manga.html', context)

def add_manga(request):
    data = {
        'form':ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Guardado Correctamente'
        data['form'] = formulario

    return render(request, 'mangastore/add_manga.html', data)

def mod_prod(request,id):
    producto = Producto.objects.get(id=id)
    data = {
        'form':ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST,instance=producto)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Modificado Correctamente'
        data['form'] = formulario

    return render(request, 'mangastore/mod_prod.html', data)

def eliminar_producto(request,id):
    producto = Producto.objects.get(id=id)
    producto.delete()

    return redirect(to="lista_manga")