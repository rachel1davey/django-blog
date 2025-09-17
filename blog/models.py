from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
STATUS = ((0, "Draft"), (1, "Published"))
"""
Stores a single blod post in relation to :model ‘auth.User‘.
"""
class Post(models.Model):
    """
    Stores a single blog post in relation to :model:`auth.User`.

    Fields:
        title (CharField)
        slug (SlugField)
        author (ForeignKey to User)
        featured_image (CloudinaryField)
        content (TextField)
        created_on (DateTimeField)
        status (IntegerField)
        excerpt (TextField)
        updated_on (DateTimeField)
    Relations:
        author: ForeignKey to User
        comments: Reverse ForeignKey from Comment
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts'
    )
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        """String representation of Post object."""
        return f"{self.title} | written by {self.author}"
       

class Comment(models.Model):
    """
    Stores a single comment on a blog post.

    Fields:
        post (ForeignKey to Post)
        author (ForeignKey to User)
        body (TextField)
        is_approved (BooleanField)
        created_on (DateTimeField)
    Relations:
        post: ForeignKey to Post
        author: ForeignKey to User
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments'
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='commenter'
    )
    body = models.TextField(null=False)
    is_approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]
    
    def __str__(self):
        """String representation of Comment object."""
        return f"Comment {self.body} by {self.author}"



