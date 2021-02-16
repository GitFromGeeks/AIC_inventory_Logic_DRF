from django.contrib import admin
from .models import credit

@admin.register(credit)
class creditAdmin(admin.ModelAdmin):
    list_display=['id','created_at','branch_code','credit']