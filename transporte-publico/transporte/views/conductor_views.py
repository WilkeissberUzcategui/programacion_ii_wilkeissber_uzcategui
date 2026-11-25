from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from transporte import Conductor


@login_required
def conductor_list(request):
    return render(request, 'transporte/conductores/lista.html', {'conductores': Conductor.objects.all()})


@login_required
def conductor_detail(request, pk):
    conductor = get_object_or_404(Conductor, pk=pk)
    return render(request, 'transporte/conductores/detalle.html', {'conductor': conductor})