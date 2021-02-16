from django.contrib import admin
from .models import stockinfo
@admin.register(stockinfo)
class stockinfoAdmin(admin.ModelAdmin):
    list_display=['id','created_at','branch_code','imei','mobile']