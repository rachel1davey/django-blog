from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class About(models.Model):
    """
    Model representing the About page content.
    """
    title = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    profile_image = CloudinaryField('image', default='placeholder')
    
    def __str__(self):
        """String representation of About object."""
        return self.title

class CollaborateRequest(models.Model):
    """
    Model representing a collaboration request.
    """
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        """String representation of CollaborateRequest object."""
        return f"Collaboration request from {self.name}"