from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404
from transporte.forms import RutaForm
from transporte.models import Ruta


@login_required
def ruta_list(request):
    return render(request, 'transporte/rutas/lista.html', {'rutas': Ruta.objects.all()})


@login_required
def ruta_detail(request, pk):
    ruta = get_object_or_404(Ruta, pk=pk)
    return render(request, 'transporte/rutas/detalle.html', {'ruta': ruta})


@login_required
@permission_required('transporte.add_ruta', raise_exception=True)
def ruta_create(request):
    if request.method == 'POST':
        form = RutaForm(request.POST)
        if form.is_valid():
            ruta = form.save(commit=False)
            ruta.creado_por = request.user
            ruta.save()
            form.save_m2m()
            messages.success(request, 'Ruta creada exitosamente.')
            return redirect('ruta_list')
    else:
        form = RutaForm()
    return render(request, 'transporte/rutas/formulario.html', {'form': form})


@login_required
@permission_required('transporte.change_ruta', raise_exception=True)
def ruta_update(request, pk):
    ruta = get_object_or_404(Ruta, pk=pk)
    if ruta.creado_por != request.user and not request.user.has_perm('transporte.delete_ruta'):
        raise PermissionDenied
    if request.method == 'POST':
        form = RutaForm(request.POST, instance=ruta)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ruta actualizada exitosamente.')
            return redirect('ruta_detail', pk=ruta.pk)
    else:
        form = RutaForm(instance=ruta)
    return render(request, 'transporte/rutas/formulario.html', {'form': form})


@login_required
@permission_required('transporte.delete_ruta', raise_exception=True)
def ruta_delete(request, pk):
    ruta = get_object_or_404(Ruta, pk=pk)
    if request.method == 'POST':
        ruta.delete()
        messages.success(request, 'Ruta eliminada exitosamente.')
        return redirect('ruta_list')
    return render(request, 'transporte/rutas/confirmar_eliminar.html', {'ruta': ruta})