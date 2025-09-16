from django.shortcuts import render
from .models import About, CollaborateRequest
from .forms import CollaborateForm


def about_me(request):
    """
    Renders the About page
    """
    about = About.objects.all().order_by('-updated_on').first()
    form = CollaborateForm()

    return render(
        request,
        "about/about.html",
        {"about": about,
         "form": form},
    )