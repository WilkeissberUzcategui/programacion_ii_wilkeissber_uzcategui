from django.shortcuts import redirect, render

# Create your views here.
from django.http import HttpResponse

from tasks.forms import ProjectForm
from tasks.models import Project


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

def leads_like(request):
    contex = {
        "titulo" : "taskflow",
        "nombre" : "Wilkeissber",
        "apellido" : "Uzcátegui"
    }
    return render(request,
                  "leads/leads-like.html",
                  contex
                  )

def base_triangulo(request, base, altura):
    """Registro usuario"""
    resultado = base*altura/2
    return HttpResponse(
        f"El àrea de un triagulo es: {resultado}")



def project_lista(request):
    contexto = {
        "titulo": "TaskFlow",
        "mensaje": "Organiza tus proyectos y tareas en un solo lugar",
        "projects": Project.objects.order_by("-created_at"),
    }
    return render(request, "projects/projects.html", contexto)


def project_create(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            task = form.save()
            return redirect("tasks:projects-list")
    else:
        form = ProjectForm()

    return render(request, "projects/project_form.html", {"form": form, "modo": "crear"})