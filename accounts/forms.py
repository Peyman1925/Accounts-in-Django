from django import forms
from .models import *

class UserProfilePictureForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['photo']
        widgets = {
            'photo': forms.FileInput(attrs={'placeholder': 'select your photo'}),
        }