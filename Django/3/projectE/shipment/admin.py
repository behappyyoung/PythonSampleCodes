from django.contrib import admin


from .models import Item, Job, 거래처

class ItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'amount']

class JobAdmin(admin.ModelAdmin):
    list_display = ['번호', '예정량']

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['코드', '거래처명']

admin.site.register(Item, ItemAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(거래처, CustomerAdmin)


