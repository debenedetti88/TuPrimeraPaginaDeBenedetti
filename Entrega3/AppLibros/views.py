from django.shortcuts import render, redirect
from .models import Libro, Autor, Editorial, Comentario
from .forms import LibroForm, EditorialForm, AutorForm, UserEditForm, ComentarioForm
from django.views.generic import ListView, UpdateView, DetailView
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login



def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'acerca_de_mi.html')

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
            return redirect('lista_libros') 
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
    
def eliminar_libro(request, libro_nombre):
    libro = Libro.objects.get(titulo=libro_nombre)
    libro.delete()
    libros = Libro.objects.all()
    return render(request, 'libros.html', {'libros': libros})


def editar_libro(request, libro_nombre):


    libro = Libro.objects.get(titulo=libro_nombre)


    if request.method == 'POST':

     
        miFormulario = LibroForm(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:  

            informacion = miFormulario.cleaned_data

            libro.titulo = informacion['titulo']
            libro.autor = informacion['autor']
            libro.editorial = informacion['editorial']
            libro.genero = informacion['genero']

            libro.save()

       
            return render(request, 'libros.html', {'libros': libros})

        else:
 
            miFormulario = LibroForm(initial={'titulo': libro.titulo, 'autor': libro.autor,'editorial': libro.editorial, 'genero': libro.genero})

    return render(request, "AppLibros/editar_libro", {"miFormulario": miFormulario, "libro": libro_nombre}, "AppLibros/editar_libro.html", {"miFormulario": miFormulario, "libro": libro})


class LibroListView(ListView):
    model = Libro 
    template_name = 'libro_lista.html'  
    context_object_name = 'libros' 


class LibroUpdateView(UpdateView):
    model = Libro  
    form_class = LibroForm 
    template_name = 'view_libro_editar.html' 


class libros_detalle(DetailView):
    model = Libro  
    template_name = 'libro_detalle.html'  
    context_object_name = 'libro'  





def login_request(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Inicio de sesion exitoso.')
            return redirect('libros') 
        else:
            messages.error(request, 'Nombre de usuario o contrasena incorrectos.')

    return render(request, 'login_request.html')


def editarPerfil(request):
    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST, instance=request.user)

        if miFormulario.is_valid():
            miFormulario.save()

            return render(request, "AppLibros/libros.html")

    else:

        miFormulario = UserEditForm(instance=request.user)

    return render(request, "AppCoder/editar_perfil.html", {"miFormulario": miFormulario, "usuario": usuario})

class CambiarContrasenia(LoginRequiredMixin, PasswordChangeView):
    template_name = 'AppLibros/cambiar_contrasena.html'
    success_url = ('editarPerfil')
    

def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'libros/lista_libros.html', {'libros': libros})


def detalle_libro(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)
    comentarios = libro.comentarios.all()
    return render(request, 'libros/detalle_libro.html', {'libro': libro, 'comentarios': comentarios})
       

@login_required
def agregar_comentario(request, libro_id):
    libro = Libro.objects.get(pk=libro_id)

    if request.method == 'POST':
        form = ComentarioForm(request.POST, request.FILES)
        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            subtitulo = form.cleaned_data['subtitulo']
            cuerpo = form.cleaned_data['cuerpo']
            autor = form.cleaned_data['autor']
            imagen = form.cleaned_data['imagen']

            comentario = Comentario(
                comentario=libro,
                titulo=titulo,
                subtitulo=subtitulo,
                cuerpo=cuerpo,
                autor=autor,
                imagen=imagen
            )
            comentario.save()

            return redirect('detalle_libro', libro_id=libro.id)
    else:
        form = ComentarioForm()

    return render(request, 'agregar_comentario.html', {'libro': libro, 'form': form})