from rest_framework import serializers
from .models import myprofile


class myprofileSerializers(serializers.ModelSerializer):
    class Meta:
        model=myprofile
        fields=['branch_code','franchise_plane','name','email','phone_number','bank_name','acc_number','ifsc_code','profile_photo','shop_add','home_add','aadhaar_number','pan_number']