from django.contrib import admin
from .models import phone


@admin.register(phone)
class phoneAdmin(admin.ModelAdmin):
    list_display=['model','mobile','ram','storage','color','price']