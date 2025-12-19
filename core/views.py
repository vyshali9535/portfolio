from django.shortcuts import render
from .models import About, Project

def home(request):
    about = About.objects.first()
    projects = Project.objects.all()

    skills = []
    if about and about.skills:
        skills = [s.strip() for s in about.skills.split(',')]  # split into a list

    context = {
        "about": about,
        "projects": projects,
        "skills": skills,
    }
    return render(request, "home.html", context)