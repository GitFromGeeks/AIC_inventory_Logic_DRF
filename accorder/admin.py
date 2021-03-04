from django.contrib import admin
from .models import acc_order


@admin.register(acc_order)
class accAdmin(admin.ModelAdmin):
    list_display=['id','created_at','branch_code','acc_name','price','quantity']
# Register your models here.
