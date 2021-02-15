from rest_framework import serializers
from .models import orders

class ordersSerializer(serializers.ModelSerializer):
    class Meta:
        model=orders
        fields=['created_at','branch_code','model','mobile','quantity','price']