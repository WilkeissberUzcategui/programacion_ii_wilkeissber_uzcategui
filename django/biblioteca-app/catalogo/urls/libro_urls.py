from django.urls import path

from catalogo.views.libro_views import (
    create_libro,
    libro_list
)

urlpatterns = [
    path('', libro_list, name='Libro_list'),

    path('create/', create_libro, name='create_libro'),
]
