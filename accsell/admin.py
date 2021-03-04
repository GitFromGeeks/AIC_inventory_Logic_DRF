from django.contrib import admin
from .models import accsell

@admin.register(accsell)
class accsellAdmin(admin.ModelAdmin):
    list_display=['id','created_at','branch_code','acc_name','customer_name','customer_number']