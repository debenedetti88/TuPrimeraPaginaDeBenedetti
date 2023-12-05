# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect, HttpResponse
from .models import Libro, Autor, Editorial
from django.contrib import messages
from .forms import LibroForm, EditorialForm, AutorForm


def index(request):
    return render(request, 'index.html')

def autores(request):
    autores = Autor.objects.all()
    return render(request, 'autores.html', {'autores': autores})

def editoriales(request):
    editoriales = Editorial.objects.all()
    return render(request, 'editoriales.html', {'editoriales': editoriales})

def libros(request):
    libros = Libro.objects.all()
    return render(request, 'libros.html', {'libros': libros})



def agregar_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('libros')  # Redirige a la URL de la vista de libros
    else:
        form = LibroForm()

    return render(request, 'agregar_libro.html', {'form': form})

def agregar_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('autores')  
    else:
        form = AutorForm()
    return render(request, 'agregar_autor.html', {'form': form})

def agregar_editorial(request):
    if request.method == 'POST':
        form = EditorialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('editoriales') 
    else:
        form = EditorialForm()
    return render(request, 'agregar_editorial.html', {'form': form})

def buscar_libros(request):
    if 'q' in request.GET:
        query = request.GET['q']
        libros = Libro.objects.filter(titulo__icontains=query) | Libro.objects.filter(autor__icontains=query)
        return render(request, 'buscar_libros.html', {'libros': libros, 'query': query})
    else:
        return render(request, 'buscar_libros.html', {'libros': None, 'query': None})
