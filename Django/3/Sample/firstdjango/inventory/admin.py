from django.contrib import admin

from .models import Item

class ItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'amount']

admin.site.register(Item, ItemAdmin)


