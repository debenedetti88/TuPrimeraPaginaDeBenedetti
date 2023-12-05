from django import forms
from .models import Libro, Autor, Editorial

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'editorial', 'genero']
        
class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'fecha_nacimiento', 'nacionalidad']

class EditorialForm(forms.ModelForm):
    class Meta:
        model = Editorial
        fields = ['nombre', 'sitio_web']
