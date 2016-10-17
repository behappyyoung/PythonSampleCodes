from django import forms
from tracker.models import Samples, Orders, SampleOrderRel, PatientOrderPhenoType, PhenoTypes, OrderGeneList
from mybackend.models import GeneLists

class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields =  '__all__'


class SampleOrderRelForm(forms.ModelForm):
    class Meta:
        model = SampleOrderRel
        fields = '__all__'


class PatientOrderPhenoTypeForm(forms.ModelForm):
    class Meta:
        model = PatientOrderPhenoType
        fields = '__all__'


class PhenoTypesForm(forms.ModelForm):
    desc = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = PhenoTypes
        fields = ('name', 'type', 'desc', 'image', 'date',)
        widgets = {
            'date': forms.TextInput(attrs={'readonly': 'readonly'})
        }


class OrderGeneListForm(forms.ModelForm):
    class Meta:
        model = OrderGeneList
        fields = '__all__'


class GeneListsForm(forms.ModelForm):
    class Meta:
        model = GeneLists
        fields = ('category', 'name','list', 'desc')

