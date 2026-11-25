from django.urls import path
from transporte import views

urlpatterns = [
    path('vehiculos/', views.vehiculo_list, name='vehiculo_list'),
    path('vehiculos/nuevo/', views.vehiculo_create, name='vehiculo_create'),
    path('vehiculos/<int:pk>/', views.vehiculo_detail, name='vehiculo_detail'),
    path('vehiculos/<int:pk>/editar/', views.vehiculo_update, name='vehiculo_update'),
    path('vehiculos/<int:pk>/eliminar/', views.vehiculo_delete, name='vehiculo_delete'),
]