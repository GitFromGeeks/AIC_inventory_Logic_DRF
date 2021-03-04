from django.contrib import admin
from .models import accinventory,accstock


@admin.register(accinventory)
class inventoryAdmin(admin.ModelAdmin):
    list_display=['id','branch_code','acc_name','quantity']

@admin.register(accstock)
class mobilestockAdmin(admin.ModelAdmin):
    list_display=['acc_name','price','quantity','amount']