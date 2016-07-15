from django.contrib import admin


from .models import Item, Job, 거래처, 현장, 출하, 수주, standard_name

class ItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'amount', 'description']

class JobAdmin(admin.ModelAdmin):
    list_display = ['번호', '예정량']

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['코드', '거래처명', '대표자']

class SiteAdmin(admin.ModelAdmin):
    list_display = ['현장명']

class ShipmentAdmin(admin.ModelAdmin):
    list_display = ['번호', 'get_customer', '예정량']
    ##list_display = ['번호', 'get_customer', '예정량','현장_id']

    def get_customer(self, obj):
        return obj.거래처.거래처명

class OrderAdmin(admin.ModelAdmin):
    list_display = ['번호', '일자']
   ## list_display= ['번호', '일자', '원청_id','현장_id']

class standard_nameAdmin(admin.ModelAdmin):
    list_display =['m40', 'm25', 'm19', 'm13','m10', 'sd', 'sb1', 'sb2']

admin.site.register(Item, ItemAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(거래처, CustomerAdmin)
admin.site.register(현장, SiteAdmin)
admin.site.register(출하, ShipmentAdmin)
admin.site.register(수주, OrderAdmin)
admin.site.register(standard_name, standard_nameAdmin)


