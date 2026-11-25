from django.urls import path
from transporte import views

urlpatterns = [
    path('conductores/', views.conductor_list, name='conductor_list'),
    path('conductores/<int:pk>/', views.conductor_detail, name='conductor_detail'),
]