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


class CategoryForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        try:
            CHOICES = Category.objects.filter()
            select_choice = [(x.id, x.name) for x in CHOICES]
            select_choice = [('','---------')] + select_choice

        except:
            select_choice = [('','---------')]
        self.fields['parent'].widget = forms.Select(choices=select_choice)

    class Meta:
        model = Category
        fields = '__all__'
