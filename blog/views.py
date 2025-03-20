from django.shortcuts import render, get_object_or_404
from .models import Publicacion, Categoria

# Create your views here.
def lista_publicaciones(request):
    publicaciones = Publicacion.objects.all()
    return render(request, 'blog/lista_publicaciones.html', {'publicaciones': publicaciones})

def detalle_publicacion(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)
    categorias = publicacion.categorias.all()
    context = {'publicacion': publicacion, 'categorias': categorias}
    return render(request, 'blog/detalle_publicacion.html', context)

def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'blog/lista_categorias.html', {'categorias': categorias})

def detalle_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    publicacion = Publicacion.objects.filter(categorias=categoria)
    context = {'categoria': categoria, 'publicacion': publicacion}
    return render(request, 'blog/detalle_categoria.html', context)