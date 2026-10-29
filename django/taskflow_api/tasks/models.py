from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    class Status(models.TextChoices):
        TODO = "TODO", "Por hacer"
        IN_PROGRESS = "IN_PROGRESS", "En progreso"
        DONE = "DONE", "Completada"

    # ForeignKey: cada Task pertenece a UN Project.
    # Un Project puede tener MUCHAS Task — relación muchos a uno.
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="tasks",
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.TODO,
    )
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class autobus(models.Model):
    aerolinea = models.CharField(max_length=100)
    tipo_bus = models.TextField(blank=True)
    horario = models.TextField(max_length=100)
    conductor = models.CharField(max_length=100)
    created_at_bus = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.aerolinea

class Sensei(models.Model):

    nombre = models.CharField(max_length=100)
    edad = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return super().nombre

class Alumno(models.Model):

    sensei = models.ForeignKey(Sensei,
                               on_delete=models.CASCADE,
                               related_name='alumnos')
    nombre = models.CharField(max_length=100)
    edad = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    misiones = models.ManyToManyField('Mision',
                                      related_name='alumnos')

    def __str__(self):
        return super().nombre

class Perfil(models.Model):

    alumno = models.OneToOneField(Alumno, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='perfiles/')
    created_at = models.DateTimeField(auto_now_add=True)


class Mision(models.Model):

    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Estudiante(models.Model):
    
    nombre = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return super().nombre

class Actividad(models.Model):

    titulo = models.CharField(max_length=100)
    objetivo = models.CharField(max_length=100)
    estudiantes = models.ManyToManyField(Estudiante,
                                         through='Participacion')

class Participacion(models.Model):
    estudiante = models.ForeignKey(Estudiante,
                                   on_delete=models.CASCADE)
    actividad = models.ForeignKey(Actividad,
                                  on_delete=models.CASCADE)
    rol = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

