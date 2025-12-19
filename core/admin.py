from django.contrib import admin
from .models import About, Project

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "link")