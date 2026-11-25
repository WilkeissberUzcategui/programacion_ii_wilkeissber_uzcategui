from django.urls import path
from transporte import views
from transporte.urls.parada_urls import urlpatterns as parada_urls
from transporte.urls.conductor_urls import urlpatterns as conductor_urls
from transporte.urls.ruta_urls import urlpatterns as ruta_urls
from transporte.urls.vehiculo_urls import urlpatterns as vehiculo_urls

auth_urls = [
    path('registro/', views.registro, name='registro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]

urlpatterns = [
    path('', views.ruta_list, name='inicio'),
] + parada_urls + conductor_urls + ruta_urls + vehiculo_urls + auth_urls