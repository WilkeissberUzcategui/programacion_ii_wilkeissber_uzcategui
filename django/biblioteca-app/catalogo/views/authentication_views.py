
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy


class BibliotecaLoginView(LoginView):
    template_name = 'catalogo/authentication/login.html'
    redirect_authenticated_user = True


class BibliotecaLogoutView(LogoutView):
    next_page = 'login'


class BibliotecaRegistroView(CreateView):
    form_class = UserCreationForm
    template_name = 'catalogo/authentication/registro.html'
    success_url = reverse_lazy('login')
