from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class About(models.Model):
    """
    Model representing the About page content.

    Fields:
        title (CharField)
        updated_on (DateTimeField)
        content (TextField)
        profile_image (CloudinaryField)
    Relations:
        None
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

    Fields:
        name (CharField)
        email (EmailField)
        message (TextField)
        read (BooleanField)
    Relations:
        None
    """
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        """String representation of CollaborateRequest object."""
        return f"Collaboration request from {self.name}"