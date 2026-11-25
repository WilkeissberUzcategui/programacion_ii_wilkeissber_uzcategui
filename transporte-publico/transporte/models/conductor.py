from django.db import models
from django.urls import reverse


class Conductor(models.Model):
    nombre = models.CharField(max_length=100)
    licencia = models.CharField(max_length=20, unique=True)
    fecha_ingreso = models.DateField()

    class Meta:
        ordering = ['nombre']
        verbose_name = 'conductor'
        verbose_name_plural = 'conductores'

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('conductor_detail', args=[self.pk])