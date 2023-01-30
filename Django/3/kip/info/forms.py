from django import forms

from .models import *

class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ('url', 'title', 'contents', 'content_type', 'content_category', 'tags')
