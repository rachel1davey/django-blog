from django.shortcuts import render
from .models import About, CollaborateRequest
from .forms import CollaborateForm
from django.contrib import messages


def about_me(request):
    """
    Renders the About page
    """
    about = About.objects.all().order_by('-updated_on').first()
    form = CollaborateForm()

    if request.method == "POST":
        form = CollaborateForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval')

    return render(
        request,
        "about/about.html",
        {"about": about,
         "form": form},
    )