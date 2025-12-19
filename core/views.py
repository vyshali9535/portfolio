from django.shortcuts import render, redirect
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
    return render(request, "index.html", context)


# NEW contact view
def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # For now, just print to console so you can see it works
        print("New message:", name, email, message)

        return redirect("contact_success")

    # GET request → show the form
    return render(request, "index.html")


# NEW success view
def contact_success(request):
    return render(request, "contact_success.html")