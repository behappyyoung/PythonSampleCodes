from django import forms

from .models import *

class ContentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ContentForm, self).__init__(*args, **kwargs)
        try:
            CHOICES = ContentType.objects.filter()
        except:
            CHOICES = []
        self.fields['content_type'].widget = forms.Select(choices=((x.id, x.type) for x in CHOICES))
        try:
            CHOICES = Category.objects.filter()
        except:
            CHOICES = []
        self.fields['content_category'].widget = forms.Select(choices=((x.id, x.name) for x in CHOICES))

    class Meta:
        model = Content
        fields = ( 'title', 'contents', 'content_type', 'content_category', 'tags')

