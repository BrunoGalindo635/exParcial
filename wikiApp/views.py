from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import TemaWiki, ArticuloWiki, TemaForm, ArticuloForm

# Create your views here.

def vista_principal(request):
    temas = TemaWiki.objects.all()
    return render(request, 'vista_principal.html', {'temas': temas})

def crear_tema(request):
    if request.method == 'POST':
        form = TemaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = TemaForm()
    temas = TemaWiki.objects.all()
    return render(request, 'crear_tema.html', {'form': form, 'temas': temas})

def crear_articulo(request):
    if request.method == 'POST':
        form = ArticuloForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = ArticuloForm()
    temas = TemaWiki.objects.all()
    return render(request, 'crear_articulo.html', {'form': form, 'temas': temas})

def articulos_por_tema(request, tema_id):
    return HttpResponse(f"Artículos del tema {tema_id}")

def ver_articulo(request, articulo_id):
    articulo = ArticuloWiki.objects.get(pk=articulo_id)
    temas = TemaWiki.objects.all()
    return render(request, 'ver_articulo.html', {'articulo': articulo, 'temas': temas})

def buscar_articulos(request):
    query = request.GET.get('q', '')
    resultados = ArticuloWiki.objects.filter(titulo__icontains=query) if query else []
    temas = TemaWiki.objects.all()
    return render(request, 'buscar.html', {'resultados': resultados, 'temas': temas})