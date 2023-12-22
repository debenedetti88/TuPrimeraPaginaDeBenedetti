from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField





class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=50)
    editorial = models.CharField(max_length=50)
    genero = models.CharField(max_length=20)   
    descripcion = RichTextField(null=True) 
    url = models.URLField(blank=True, null=True)  
    imagen = models.ImageField(upload_to='imagenes_libros', null=True, blank=True)

    def __str__(self):
        return f"Titulo: {self.titulo} - Autor {self.autor} - Editorial {self.editorial} - Genero {self.genero}"

class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    nacionalidad = models.CharField(max_length=50)
    

class Editorial(models.Model):
    nombre = models.CharField(max_length=50)
    sitio_web = models.CharField(max_length=50)
    

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)
    def __str__(self):
        return f"{self.user} - {self.imagen}"
from django.db import models

class Comentario(models.Model):
    comentario = models.ForeignKey(Libro, related_name='comentarios', on_delete=models.CASCADE, null=True)
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=100, null=True, blank=True)
    cuerpo = models.TextField(null=True, blank=True)
    autor = models.CharField(max_length=40)
    fechaComentario = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='comentario_imagenes/', null=True, blank=True)

    class Meta:
        ordering = ['-fechaComentario']

    def __str__(self):
        return self.titulo
