from django.shortcuts import render

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