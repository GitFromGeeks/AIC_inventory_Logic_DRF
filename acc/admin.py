from django.contrib import admin
from .models import accessorie

@admin.register(accessorie)
class accAdmin(admin.ModelAdmin):
    list_display=['acc_name','price']
# Register your models here.
