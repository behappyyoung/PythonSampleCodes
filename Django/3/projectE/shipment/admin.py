from django.contrib import admin


from .models import Item, Job, 거래처, 현장, 출하, 수주, standard_name, contracts, sites, customers, standard

class ItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'amount', 'description']

class JobAdmin(admin.ModelAdmin):
    list_display = ['번호', '예정량']



class ShipmentAdmin(admin.ModelAdmin):
    list_display = ['번호', 'get_customer', '예정량']

    def get_customer(self, obj):
        return obj.거래처.거래처명



class CustomersInline(admin.TabularInline):
    model = customers

class SitesAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'customer', 'get_customer']

    def get_customer(self, obj):
        return obj.customer.name
##    inlines = [        CustomersInline,    ]

class CustomersAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'chief', 'manager']


class contractsAdmin(admin.ModelAdmin):
    list_display = ['number', 'date', 'order_customer', 'sub_customer', 'site']

class standard_nameAdmin(admin.ModelAdmin):
    list_display =['m40', 'm25', 'm19', 'm13','m10', 'sd', 'sb1', 'sb2']

class standardAdmin(admin.ModelAdmin):
    list_diplay = ['name', 'standard_name', 'price', 'cost']

admin.site.register(Item, ItemAdmin)
admin.site.register(Job, JobAdmin)
#admin.site.register(거래처, CustomerAdmin)
#admin.site.register(현장, SiteAdmin)
admin.site.register(출하, ShipmentAdmin)
#admin.site.register(수주, OrderAdmin)
admin.site.register(standard, standardAdmin)
admin.site.register(standard_name, standard_nameAdmin)
admin.site.register(customers, CustomersAdmin)
admin.site.register(sites, SitesAdmin)
admin.site.register(contracts, contractsAdmin)

