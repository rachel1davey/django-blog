from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post
from django.contrib import messages
from .forms import CommentForm

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
    comment_form = CommentForm()

    if request.method == "POST":
      comment_form = CommentForm(data=request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.author = request.user
        comment.post = post
        comment.save()
        messages.add_message(
        request, messages.SUCCESS,
        'Comment submitted and awaiting approval'
    )

        


    return render(
        request,
        "blog/post_detail.html",
        {"post": post, 
         "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,},
    )    