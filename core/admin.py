from django.contrib import admin
from .models import About, Project, ContactMessage

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "link")

# core/admin.py

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "message", "created_at")