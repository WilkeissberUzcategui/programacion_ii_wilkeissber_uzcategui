from django.contrib import admin
from transporte import Parada, Conductor, Ruta, Vehiculo


@admin.register(Parada)
class ParadaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'direccion']
    list_filter = ['nombre']
    search_fields = ['nombre', 'direccion']


@admin.register(Conductor)
class ConductorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'licencia', 'fecha_ingreso']
    list_filter = ['fecha_ingreso']
    search_fields = ['nombre', 'licencia']


@admin.register(Ruta)
class RutaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'origen', 'destino', 'tarifa', 'creado_por']
    list_filter = ['creado_por', 'origen']
    search_fields = ['nombre', 'origen', 'destino']


@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ['placa', 'tipo', 'capacidad', 'activo', 'ruta']
    list_filter = ['tipo', 'activo', 'ruta']
    search_fields = ['placa']