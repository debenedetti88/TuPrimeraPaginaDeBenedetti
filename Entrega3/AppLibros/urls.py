from django.urls import path
from . import views
from accounts import views as v
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.index, name='index'),
    path('AppLibros/libros/', views.libros, name='libros'),
    path('AppLibros/autores/', views.autores, name='autores'),
    path('AppLibros/editoriales/', views.editoriales, name='editoriales'),
    path('AppLibros/agregar_libro/', views.agregar_libro, name='agregar_libro'),
    path('AppLibros/agregar_autor/', views.agregar_autor, name='agregar_autor'),
    path('AppLibros/agregar_editorial/', views.agregar_editorial, name='agregar_editorial'),
    path('AppLibros/buscar_libros/', views.buscar_libros, name='buscar_libros'),
    path('AppLibros/login_request/', views.login_request, name="login_request"),
    path('AppLibros/cambiar_constrasena/', views.CambiarContrasenia.as_view(), name="cambiar_constrasena"),
    path('libros/', views.lista_libros, name='lista_libros'),
    path('libros/<int:libro_id>/', views.detalle_libro, name='detalle_libro'),
    path('libros/<int:libro_id>/agregar_comentario/', views.agregar_comentario, name='agregar_comentario'),
    path('acerca_de_mi/', views.about, name='acerca_de_mi'),
    path('account/view_profile/', v.view_profile, name='view_profile'),
    path('account/delete_profile/', v.delete_profile, name='delete_profile'),
    path('account/edicionPerfil/<int:pk>/', v.UsuarioEdicion.as_view(), name='edicionPerfil'),
    path('logout/', LogoutView.as_view(next_page='despedida'), name='logout'),
    path('despedida/', v.DespedidaView.as_view(), name='despedida'),
            ]


urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
