from django.db import models
from django.urls import reverse


class Parada(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)

    class Meta:
        ordering = ['nombre']
        verbose_name = 'parada'
        verbose_name_plural = 'paradas'

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('parada_detail', args=[self.pk])