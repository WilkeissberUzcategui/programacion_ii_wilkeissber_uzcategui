from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Ruta(models.Model):
    nombre = models.CharField(max_length=100)
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    distancia = models.DecimalField(max_digits=6, decimal_places=2)
    tarifa = models.DecimalField(max_digits=5, decimal_places=2)
    paradas = models.ManyToManyField('transporte.Parada', related_name='rutas', blank=True)
    creado_por = models.ForeignKey(User, on_delete=models.PROTECT, related_name='rutas_creadas')

    class Meta:
        ordering = ['nombre']
        verbose_name = 'ruta'
        verbose_name_plural = 'rutas'

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('ruta_detail', args=[self.pk])