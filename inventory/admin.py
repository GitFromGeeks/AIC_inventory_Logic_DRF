from django.contrib import admin
from .models import inventory,mobilestock,transferstock,returninfo,transfermobile


@admin.register(inventory)
class inventoryAdmin(admin.ModelAdmin):
    list_display=['id','branch_code','model','mobile','quantity']

@admin.register(mobilestock)
class mobilestockAdmin(admin.ModelAdmin):
    list_display=['mobile','model','price','quantity','amount']

@admin.register(transferstock)
class transferstockAdmin(admin.ModelAdmin):
    list_display=['id','created_at','frombranch','tobranch','model']

@admin.register(returninfo)
class returninfoAdmin(admin.ModelAdmin):
    list_display=['id','created_at','branch_code','mobile','price']

@admin.register(transfermobile)
class transfermobileAdmin(admin.ModelAdmin):
    list_display=['id','created_at','frombranch','tobranch','model','price']
    