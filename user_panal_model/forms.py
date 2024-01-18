from django import forms
from django.core import validators

from User_module.models import User


class EmailForms(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', ]


class EditProfileModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'Resume_Link', 'avatar', 'about_user']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'avatar': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'Resume_Link': forms.URLInput(attrs={
                'class': 'form-control'
            }),

            'about_user': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 6,

            }),
        }

        labels = {
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'Resume_Link': 'لینک رزومه',
            'avatar': 'تصویر پروفایل',
            'about_user': 'درباره شخص'
        }
