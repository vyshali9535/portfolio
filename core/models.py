from django.db import models

class About(models.Model):
    name = models.CharField(max_length=100)         # your name
    bio = models.TextField()                         # short introduction
    skills = models.TextField(                       # comma-separated skills
        help_text="Comma-separated skills (e.g., Python, Django, SQL)"
    )

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=100)         # project title
    description = models.TextField()                 # project details
    link = models.URLField(blank=True)               # optional link (GitHub, website)
    image = models.ImageField(upload_to='projects/', blank=True)  # optional image

    def __str__(self):
        return self.title