from django.contrib import admin
from .models import sell

@admin.register(sell)
class sellAdmin(admin.ModelAdmin):
    list_display=['id','created_at','branch_code','model','mobile','customer_name','customer_number']





    # ,'customer_add','dp','emi','loan_id','imei'