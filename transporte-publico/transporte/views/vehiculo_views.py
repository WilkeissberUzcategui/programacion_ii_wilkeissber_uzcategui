from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404
from transporte.forms import VehiculoForm
from transporte import Vehiculo


@login_required
def vehiculo_list(request):
    return render(request, 'transporte/vehiculos/lista.html', {'vehiculos': Vehiculo.objects.all()})


@login_required
def vehiculo_detail(request, pk):
    vehiculo = get_object_or_404(Vehiculo, pk=pk)
    return render(request, 'transporte/vehiculos/detalle.html', {'vehiculo': vehiculo})


@login_required
@permission_required('transporte.add_vehiculo', raise_exception=True)
def vehiculo_create(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            vehiculo = form.save(commit=False)
            vehiculo.creado_por = request.user
            vehiculo.save()
            messages.success(request, 'Vehículo creado exitosamente.')
            return redirect('vehiculo_list')
    else:
        form = VehiculoForm()
    return render(request, 'transporte/vehiculos/formulario.html', {'form': form})


@login_required
@permission_required('transporte.change_vehiculo', raise_exception=True)
def vehiculo_update(request, pk):
    vehiculo = get_object_or_404(Vehiculo, pk=pk)
    if vehiculo.creado_por != request.user and not request.user.has_perm('transporte.delete_vehiculo'):
        raise PermissionDenied
    if request.method == 'POST':
        form = VehiculoForm(request.POST, instance=vehiculo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vehículo actualizado exitosamente.')
            return redirect('vehiculo_detail', pk=vehiculo.pk)
    else:
        form = VehiculoForm(instance=vehiculo)
    return render(request, 'transporte/vehiculos/formulario.html', {'form': form})


@login_required
@permission_required('transporte.delete_vehiculo', raise_exception=True)
def vehiculo_delete(request, pk):
    vehiculo = get_object_or_404(Vehiculo, pk=pk)
    if request.method == 'POST':
        vehiculo.delete()
        messages.success(request, 'Vehículo eliminado exitosamente.')
        return redirect('vehiculo_list')
    return render(request, 'transporte/vehiculos/confirmar_eliminar.html', {'vehiculo': vehiculo})