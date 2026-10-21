from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    """Vista de bienvenida de la app tasks."""
    return HttpResponse("""
        <html>
            <body>
                <h1>TaskFlow</h1>
                <p>Bienvenido al sistema</p>
            </body>
        </html>
    """)

def register(request):
    """Registro de usuarios."""
    return HttpResponse("Registro de usuario en linea")

def primera(request):
    """Mi primera funcion realizada"""
    return HttpResponse("Mi primera pruba hecha por mi persona")

def about_me(request):
    '''Mi persona'''
    return HttpResponse("Estudiante de Ing Informatica")

def greeting(request, nombre):
    """Saludo"""
    return HttpResponse(
        f"Hola {nombre}, bienvenido a mi pagina web")

def destinatario(request, titulo, nombre, cargo):
    """Saludo"""
    return HttpResponse(
        f"bienvenido: {titulo} {nombre}, su cargo es {cargo}")

def my_first_template(request):
    contexto = {
        "titulo": "TaskFlow",
        "mensaje": "Organiza tus proyectos y tareas en un solo lugar",
    }
    return render(request, "tasks/my_first_template.html", contexto)