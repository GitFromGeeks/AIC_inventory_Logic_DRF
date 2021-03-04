from rest_framework import serializers
from .models import acc_order


class accSerializer(serializers.ModelSerializer):
    class Meta:
        model=acc_order
        fields=['id','created_at','branch_code','acc_name','price','quantity']