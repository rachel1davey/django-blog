from django import forms
from .models import CollaborateRequest

class CollaborateForm(forms.modelForm):
    class Meta:
        model = collab
        fields = ('name', 'email', 'message',)