from django.contrib import admin
from .models import orders


@admin.register(orders)
class ordersAdmin(admin.ModelAdmin):
    list_display=['id','created_at','branch_code','model','mobile','quantity','price']