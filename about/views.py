from django.shortcuts import render
from .models import About, CollaborateRequest
from .forms import CollaborateForm
from django.contrib import messages


def about_me(request):
    """
    Renders the About page and handles collaboration form submission.
    Args:
        request: Django HttpRequest object.
    Returns:
        Rendered about page with form and messages.
    """
    about = About.objects.all().order_by('-updated_on').first()
    form = CollaborateForm()

    if request.method == "POST":
        form = CollaborateForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Collaboration request received! I endeavor to respond within 2 working days.')

    return render(
        request,
        "about/about.html",
        {"about": about,
         "form": form},
    )