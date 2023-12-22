from django.urls import reverse
from django.views.generic import TemplateView, UpdateView
from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST
from .models import UserProfile
from .forms import  FormularioEdicion, FormularioRegistroUsuario, UserProfileForm, CambiarContrasenaForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

class LoginPagina(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    success_url = reverse_lazy('index')

    def get_success_url(self):
        return reverse_lazy('index')

class RegistroPagina(FormView):
    template_name = 'registro.html'
    form_class = FormularioRegistroUsuario
    redirect_authenticated_user = False

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegistroPagina, self).form_valid(form)

    def get_success_url(self):
        return reverse('edicionPerfil', kwargs={'pk': self.request.user.pk})

    def get(self, *args, **kwargs):
        return super(RegistroPagina, self).get(*args, **kwargs)

class UsuarioEdicion(SuccessMessageMixin, PasswordChangeView):
    form_class = FormularioEdicion
    template_name = 'edicionPerfil.html'
    success_url = reverse_lazy('libros')
    success_message = 'Perfil actualizado exitosamente.'

    def get_object(self):
        return self.request.user

class UpdateProfileView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'edit_profile.html'
    success_url = reverse_lazy('view_profile')

    def get_object(self):
        return self.request.user.userprofile

@login_required
def view_profile(request):
    user_profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        if 'password_change' in request.POST:
            password_form = CambiarContrasenaForm(request.user, request.POST)
            user_form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
            if password_form.is_valid() and user_form.is_valid():
                password_form.save()
                user_form.save()
                return redirect('view_profile')
        else:
            user_form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
            if user_form.is_valid():
                user_form.save()
                return redirect('view_profile')
    else:
        user_form = UserProfileForm(instance=user_profile)
        password_form = CambiarContrasenaForm(request.user)

    return render(request, 'view_profile.html', {'user_form': user_form, 'password_form': password_form})

@login_required
@require_POST
def delete_profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    user_profile.delete()
    return redirect('index') 

def logout_view(request):
    logout(request)
    return redirect('index')

class DespedidaView(TemplateView):
    template_name = 'despedida.html'
    
class CambioPassword(SuccessMessageMixin, PasswordChangeView):
    template_name = 'cambio_password.html'
    success_url = reverse_lazy('confirmacion_cambio_contrasena')
    success_message = 'Contrasena cambiada exitosamente.'
    
def password_exitoso(request):
    return render(request, 'password_exitoso.html')
