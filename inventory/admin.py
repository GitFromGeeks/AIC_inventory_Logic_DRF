from django.contrib import admin
from .models import inventory


@admin.register(inventory)
class inventoryAdmin(admin.ModelAdmin):
    list_display=['branch_code','model','mobile','quantity']