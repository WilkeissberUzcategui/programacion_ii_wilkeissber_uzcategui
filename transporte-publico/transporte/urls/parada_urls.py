from django.urls import path
from transporte import views

urlpatterns = [
    path('paradas/', views.parada_list, name='parada_list'),
    path('paradas/<int:pk>/', views.parada_detail, name='parada_detail'),
]