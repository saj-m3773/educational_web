from django import forms
from . import models

class RegisterForms(forms.ModelForm):
    class Meta:
        model=models.User
        fields=['mobile']

