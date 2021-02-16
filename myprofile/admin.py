from django.contrib import admin
from  .models import myprofile

@admin.register(myprofile)
class myprofileAdmin(admin.ModelAdmin):
    list_display=['branch_code','franchise_plane','name','email','phone_number','password','bank_name','acc_number','ifsc_code','profile_photo','shop_add','home_add','aadhaar_number','pan_number']