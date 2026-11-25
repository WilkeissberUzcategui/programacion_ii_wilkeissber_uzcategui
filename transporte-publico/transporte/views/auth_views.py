from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.utils.http import url_has_allowed_host_and_scheme
from django.views.decorators.http import require_POST
from transporte.forms import RegistroForm


def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registro exitoso. Bienvenido.')
            return redirect(settings.LOGIN_REDIRECT_URL)
    else:
        form = RegistroForm()
    return render(request, 'transporte/auth/registro.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            destino = request.GET.get('next', '')
            if not url_has_allowed_host_and_scheme(destino, allowed_hosts={request.get_host()}):
                destino = settings.LOGIN_REDIRECT_URL
            return redirect(destino)
    else:
        form = AuthenticationForm()
    return render(request, 'transporte/auth/login.html', {'form': form})


@require_POST
def logout_view(request):
    logout(request)
    return redirect(settings.LOGOUT_REDIRECT_URL)