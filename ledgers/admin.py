from django.contrib import admin
from .models import ledgers,debth

@admin.register(ledgers)
class ledgersAdmin(admin.ModelAdmin):
    list_display=['id','created_at','branch_code','mobile','model','quantity','price','credit','debit']


@admin.register(debth)
class debthAdmin(admin.ModelAdmin):
    list_display=['branch_code','debth']
