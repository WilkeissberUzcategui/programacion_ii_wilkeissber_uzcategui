from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from transporte import Parada


@login_required
def parada_list(request):
    return render(request, 'transporte/paradas/lista.html', {'paradas': Parada.objects.all()})


@login_required
def parada_detail(request, pk):
    parada = get_object_or_404(Parada, pk=pk)
    return render(request, 'transporte/paradas/detalle.html', {'parada': parada})