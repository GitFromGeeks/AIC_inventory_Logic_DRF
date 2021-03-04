from django.contrib import admin
from .models import inventory,mobilestock


@admin.register(inventory)
class inventoryAdmin(admin.ModelAdmin):
    list_display=['id','branch_code','model','mobile','quantity']

@admin.register(mobilestock)
class mobilestockAdmin(admin.ModelAdmin):
    list_display=['mobile','model','price','quantity','amount']