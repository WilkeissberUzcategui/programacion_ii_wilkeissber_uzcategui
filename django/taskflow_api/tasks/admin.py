# Register your models here.

from django.contrib import admin
from .models import Project, autobus, Task


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name",)


@admin.register(autobus)
class AutobusAdmin(admin.ModelAdmin):
    list_display = ("aerolinea", "created_at_bus", "tipo_bus")
    search_fields = ("conductor",)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "project", "status", "due_date")
    list_filter = ("status", "project")
    search_fields = ("title", "description")