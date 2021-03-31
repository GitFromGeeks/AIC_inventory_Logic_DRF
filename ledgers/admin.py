from django.contrib import admin
from .models import ledgers,debth,account,debit

@admin.register(ledgers)
class ledgersAdmin(admin.ModelAdmin):
    list_display=['id','created_at','branch_code','mobile','model','quantity','price','credit','debit']


@admin.register(debth)
class debthAdmin(admin.ModelAdmin):
    list_display=['branch_code','debth']

@admin.register(account)
class accountsAdmin(admin.ModelAdmin):
    list_display=['id','created_at','branch_code','aicin','aicout','description']

@admin.register(debit)
class debitAdmin(admin.ModelAdmin):
    list_display=['branch_code','debit']
