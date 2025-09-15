from django.shortcuts import render, get_object_or_404
from .models import about
# Create your views here.

def about(request):

    content = about.objects.order_by("title", "content", "updated_on").first()
    about = get_object_or_404(content)
    return (request, 'about.html', {"about": about})