from django.urls import path
from transporte import views

urlpatterns = [
    path('rutas/', views.ruta_list, name='ruta_list'),
    path('rutas/nueva/', views.ruta_create, name='ruta_create'),
    path('rutas/<int:pk>/', views.ruta_detail, name='ruta_detail'),
    path('rutas/<int:pk>/editar/', views.ruta_update, name='ruta_update'),
    path('rutas/<int:pk>/eliminar/', views.ruta_delete, name='ruta_delete'),
]