
from django.urls import path
from catalogo.views.authentication_views import (
    BibliotecaLoginView,
    BibliotecaLogoutView,
    BibliotecaRegistroView
)

urlpatterns = [
    path('login/', BibliotecaLoginView.as_view(), name='login'),
    path('logout/', BibliotecaLogoutView.as_view(), name='logout'),
    path('registro/', BibliotecaRegistroView.as_view(), name='registro'),
]
