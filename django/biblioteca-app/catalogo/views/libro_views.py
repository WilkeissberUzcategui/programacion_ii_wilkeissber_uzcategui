from django.shortcuts import render, redirect
from django.contrib import messages
from catalogo.forms.libro_form import LibroForm
from catalogo.models import Libro


def libro_list(request):
    libros = Libro.objects.all()

    return render(
        request,
        'catalogo/libros/libro_list.html',
        {'libros': libros}
    )


def create_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Libro registrado exitosamente.'
            )
            return redirect('Libro_list')
    else:
        form = LibroForm()

    return render(
        request,
        'catalogo/libros/libro_form.html',
        {'form': form}
    )
