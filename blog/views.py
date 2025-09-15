from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post
# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = 'blog/index.html'
    paginate_by = 6

def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1) # filters through published posts as query set
    post = get_object_or_404(queryset, slug=slug) # post get object. basically means get object or return a http404 exception if it doesnt exist
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(is_approved=True).count()

    return render(
        request,
        "blog/post_detail.html",
        {"post": post, 
         "comments": comments,
        "comment_count": comment_count,},
    )    