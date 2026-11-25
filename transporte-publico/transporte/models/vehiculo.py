from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Vehiculo(models.Model):
    class Tipo(models.TextChoices):
        BUS = 'BUS', 'Bus'
        METRO = 'METRO', 'Metro'

    placa = models.CharField(max_length=10, unique=True)
    tipo = models.CharField(max_length=5, choices=Tipo.choices, default=Tipo.BUS)
    capacidad = models.PositiveIntegerField()
    activo = models.BooleanField(default=True)
    ruta = models.ForeignKey('transporte.Ruta', on_delete=models.CASCADE, related_name='vehiculos')
    conductor = models.ForeignKey('transporte.Conductor', on_delete=models.SET_NULL,
                                  null=True, blank=True, related_name='vehiculos')
    creado_por = models.ForeignKey(User, on_delete=models.PROTECT, related_name='vehiculos_creados')

    class Meta:
        ordering = ['placa']
        verbose_name = 'vehículo'
        verbose_name_plural = 'vehículos'

    def __str__(self):
        return f'{self.placa} ({self.get_tipo_display()})'

    def get_absolute_url(self):
        return reverse('vehiculo_detail', args=[self.pk])