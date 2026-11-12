from django.shortcuts import render, redirect
from django.contrib import messages
from catalogo.forms.autores_form import AutorForm
from catalogo.models import Autor
from django.contrib.auth.decorators import login_required, permission_required


@login_required
@permission_required('catalogo.view_autor', raise_exception=True)
def autor_list(request):
    autor = Autor.objects.all()
    return render(request, 
                  'catalogo/autores/autor_list.html', 
                  {'autor': autor})

@login_required
@permission_required('catalogo.add_autor', raise_exception=True)
def autor_create(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'autor creada exitosamente.')
            return redirect('autor_list')
    else:
        form = AutorForm()
    return render(request, 
                  'catalogo/autores/formulario.html', 
                  {'form': form})
@login_required
@permission_required('catalogo.change_autor', raise_exception=True)
def autor_update(request, pk):
    autor = Autor.objects.get(pk=pk)
    if request.method == 'POST':
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            messages.success(request, 'autor actualizada exitosamente.')
            return redirect('autor_list')
    else:
        form = AutorForm(instance=autor)
    return render(request, 
                  'catalogo/autores/formulario.html', 
                  {'form': form})

@login_required
@permission_required('catalogo.delete_autor', raise_exception=True)
def autor_delete(request, pk):
    autor = Autor.objects.get(pk=pk)
    if request.method == 'POST':
        autor.delete()
        messages.success(request, 'autor eliminada exitosamente.')
        return redirect('autor_list')
    return render(request, 
                  'catalogo/autores/autor_confirm_delete.html', 
                  {'autor': autor})
