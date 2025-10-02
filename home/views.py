from django.shortcuts import render
from . models import Skill


def index(request):
    """View to show the website homepage"""

    skills = Skill.objects.all()

    context = {
        "skills": skills,
    }

    return render(
        request,
        "home/index.html",
        context,
    )
