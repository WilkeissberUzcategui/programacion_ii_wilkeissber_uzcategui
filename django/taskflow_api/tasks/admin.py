# Register your models here.

from django.contrib import admin
from .models import Project, autobus


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name",)

@admin.register(autobus)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("aerolinea", "created_at_bus", "tipo_bus")
    search_fields = ("conductor",)