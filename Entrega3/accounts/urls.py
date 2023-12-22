from django import views
from django.urls import path
from .views import  LoginPagina, RegistroPagina, UsuarioEdicion, CambioPassword, HomeView
from django.contrib.auth.views import LogoutView
from . import views
from .views import view_profile, UpdateProfileView

urlpatterns = [
    path('login/', LoginPagina.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registro/', RegistroPagina.as_view(), name='registro'),
    path('edicionPerfil/', UsuarioEdicion.as_view(), name='editar_perfil'),
    path('passwordCambio/', CambioPassword.as_view(), name='cambiar_password'),
    path('passwordExitoso/', views.password_exitoso, name='password_exitoso'),
    path('index/', HomeView.as_view(), name='index'),
    path('account/view_profile/', view_profile, name='view_profile'),
    path('account/edit_profile/', UpdateProfileView.as_view(), name='edit_profile'),
    path('account/delete_profile/', views.delete_profile, name='delete_profile'),
    path('despedida/', views.DespedidaView.as_view(), name='despedida'),
]
