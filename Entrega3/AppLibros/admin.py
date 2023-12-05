from django.contrib import admin
from .models import Libro, Editorial, Autor

@admin.register(Libro)
class CursoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "editorial", "genero")
    list_filter = ("titulo", "autor", "editorial", "genero")
    search_fields = ("titulo", "autor", "editorial", "genero")
    
@admin.register(Editorial)
class CursoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "sitio_web")
    list_filter = ("nombre", "sitio_web")
    search_fields = ("nombre", "sitio_web")
    
@admin.register(Autor)
class CursoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "fecha_nacimiento", "nacionalidad")
    list_filter = ("nombre", "fecha_nacimiento", "nacionalidad")
    search_fields = ("nombre", "fecha_nacimiento", "nacionalidad")
    