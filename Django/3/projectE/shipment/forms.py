#from django import forms

from django.forms import ModelForm
from shipment.models import sites

#
# class SitesForm(forms.Form):
#     def __init__(self, *args, **kwargs):
#         my_arg = kwargs.pop('my_arg')
#         super(SitesForm, self).__init__(*args, **kwargs)
#     code = forms.CharField(max_length=100)
#     name = forms.CharField(max_length=100)
#     address = forms.CharField(max_length=200)

class SitesForm(ModelForm):
    class Meta:
        model = sites
        fields = ['code', 'name', 'address']
        labels = {
            'code':'코 드',
            'name':'현 장 명',
            'address':'주소'
        }

