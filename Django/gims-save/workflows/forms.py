
from django import forms
from .models import Workflows


class WorkflowsForm(forms.ModelForm):
    inputs = forms.CharField(widget=forms.Textarea)
    fixed_inputs = forms.CharField(widget=forms.Textarea)
    desc = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Workflows
        fields =  '__all__'

