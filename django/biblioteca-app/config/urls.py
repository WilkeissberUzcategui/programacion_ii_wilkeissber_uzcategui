from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),

    path(
        'catalogo/categorias/',
        include('catalogo.urls.categoria_urls')
    ),

    path(
        'catalogo/libros/',
        include('catalogo.urls.libro_urls')
    ),
]
