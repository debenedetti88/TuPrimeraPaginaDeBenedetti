from django import forms
from .models import Libro, Autor, Editorial
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'editorial', 'genero', 'descripcion', 'url', 'imagen']

    # widgets = {
    #     'descripcion': RichTextFormField(required=False),
    #     'url': forms.URLInput(attrs={'size': 40}),
    # }

        
class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'fecha_nacimiento', 'nacionalidad']

class EditorialForm(forms.ModelForm):
    class Meta:
        model = Editorial
        fields = ['nombre', 'sitio_web']
        


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contrasena", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contrasena", widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}
        

class UserEditForm(UserChangeForm):
    
    password = None
    email = forms.EmailField(label="Ingrese su email:")
    last_name = forms.CharField(label='Apellido')
    first_name = forms.CharField(label='Nombre')


    class Meta:
        model = User
        fields = ['email', 'last_name', 'first_name']



class ComentarioForm(forms.Form):
    titulo = forms.CharField(max_length=100)
    subtitulo = forms.CharField(max_length=100, required=False)
    cuerpo = forms.CharField(widget=forms.Textarea, required=False)
    autor = forms.CharField(max_length=40)
    imagen = forms.ImageField(required=False)
