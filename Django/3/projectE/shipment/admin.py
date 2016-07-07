from django.contrib import admin


from .models import Item, Job, 거래처, 현장, 출하

class ItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'amount']

class JobAdmin(admin.ModelAdmin):
    list_display = ['번호', '예정량']

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['코드', '거래처명']

class SiteAdmin(admin.ModelAdmin):
    list_display = ['현장명']

class ShipmentAdmin(admin.ModelAdmin):
    list_display = ['번호', 'get_customer', '예정량','현장']

    def get_customer(self, obj):
        return obj.거래처.거래처명



admin.site.register(Item, ItemAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(거래처, CustomerAdmin)
admin.site.register(현장, SiteAdmin)
admin.site.register(출하, ShipmentAdmin)


