from rest_framework import serializers
from .models import accsell

class accsellSerializers(serializers.ModelSerializer):
    class Meta:
        model=accsell
        fields=['id','created_at','branch_code','acc_name','customer_name','customer_number']