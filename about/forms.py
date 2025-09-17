from django import forms
from .models import CollaborateRequest

class CollaborateForm(forms.ModelForm):
    """
    Form for submitting a collaboration request.
    """
    class Meta:
        model = CollaborateRequest
        fields = ('name', 'email', 'message')