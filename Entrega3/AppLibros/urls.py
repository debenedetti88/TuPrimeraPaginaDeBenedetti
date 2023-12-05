# -*- coding: utf-8 -*-
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('AppLibros/libros/', views.libros, name='libros'),
    path('AppLibros/autores/', views.autores, name='autores'),
    path('AppLibros/editoriales/', views.editoriales, name='editoriales'),
    path('AppLibros/agregar_libro/', views.agregar_libro, name='agregar_libro'),
    path('AppLibros/agregar_autor/', views.agregar_autor, name='agregar_autor'),
    path('AppLibros/agregar_editorial/', views.agregar_editorial, name='agregar_editorial'),
    path('AppLibros/buscar_libros/', views.buscar_libros, name='buscar_libros'),
    
    ]
