from django.shortcuts import render

def index(request):
    """View to show the website homepage"""

    return render(
        request,
        "home/index.html",
    )