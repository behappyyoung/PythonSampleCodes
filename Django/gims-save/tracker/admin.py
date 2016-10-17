from django.contrib import admin
from django import forms

# Register your models here.
from .models import TrackingLog, Samples, Orders, OrderStatus, OrderType, Relations, SampleOrderRel, SampleFiles, Patients, PhenoTypes, PatientOrderPhenoList, PatientOrderPhenoType


class TrackingAdmin(admin.ModelAdmin):
    list_display = ['date', 'owner', 'sample']

    def get_sample(self, obj):
        return obj.sample.number


class SampleAdmin(admin.ModelAdmin):
    list_display = ['asn', 'number', 'type']

class SampleFileAdmin(admin.ModelAdmin):
    list_display = ['sample', 'channel_name', 'file_location', 'loom_id', 'file_type']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_name', 'patient_id', 'order_date', 'due_date', 'status']


class StatusAdmin(admin.ModelAdmin):
    list_display = ['status', 'status_name']


class OrderTypeAdmin(admin.ModelAdmin):
    list_display = ['type', 'type_name']


class RelationsAdmin(admin.ModelAdmin):
    list_display = ['rel', 'rel_name']


class SORelationsAdmin(admin.ModelAdmin):
    list_display = ['order', 'sample', 'relation']


class PatientsAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'mrn', 'dob', 'race', 'sex']


class PhenoModelForm(forms.ModelForm):
    desc = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = PhenoTypes
        fields = '__all__'


class PhenoAdmin(admin.ModelAdmin):
    list_display = ['name', 'date', 'type', 'desc', 'image']
    form = PhenoModelForm


class PatientOrderPhenoListAdmin(admin.ModelAdmin):
    list_display =  [ 'order', 'pheno_checklists', 'pheno_valuelists']

# class PatientOrderPhenoTypeAdmin(admin.ModelAdmin):
#     list_display = ['patient', 'order', 'phenotype']

admin.site.register(Samples, SampleAdmin)
admin.site.register(SampleFiles, SampleFileAdmin)
admin.site.register(Orders, OrderAdmin)
admin.site.register(TrackingLog, TrackingAdmin)
admin.site.register(OrderStatus, StatusAdmin)
admin.site.register(OrderType, OrderTypeAdmin)
admin.site.register(Relations, RelationsAdmin)
admin.site.register(SampleOrderRel, SORelationsAdmin)
admin.site.register(Patients, PatientsAdmin)
admin.site.register(PhenoTypes, PhenoAdmin)
admin.site.register(PatientOrderPhenoList, PatientOrderPhenoListAdmin)