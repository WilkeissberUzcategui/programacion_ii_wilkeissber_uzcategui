from django.urls import path
from . import views

app_name = "tasks"  

urlpatterns = [
    path("", views.home, name="home"),
    path("register", views.register, name="register"),
    path("primera", views.primera, name="primera"),
    path("aboutme", views.about_me, name="about_me"),
    path("saludo/<str:nombre>/",
         views.greeting, name="saludo"),
    path("destinatario/<str:titulo>/<str:nombre>/<str:cargo>/",
         views.destinatario, name="destinatario"),
    path("my_first_template", views.my_first_template, name="my_first_template"),
    path("leads_like", views.leads_like, name="leads_like"),
    path("base_triangulo/<int:base>/<int:altura>/",
         views.base_triangulo, name="base_triangulo"),
    ]