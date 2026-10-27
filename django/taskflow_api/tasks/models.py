from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description

class autobus(models.Model):
    aerolinea = models.CharField(max_length=100)
    tipo_bus = models.TextField(blank=True)
    horario = models.TextField(max_length=100)
    conductor = models.CharField(max_length=100)
    created_at_bus = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.aerolinea