from django.shortcuts import render, redirect
from .models import About, Project, ContactMessage

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

        # Save to database
        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message
        )

        # Redirect to a success page
        return redirect("contact_success")   # ✅ redirect properly

    return render(request, "index.html")


# NEW success view (separate function)
def contact_success(request):
    return render(request, "contact_success.html")