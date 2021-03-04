from rest_framework import serializers
from .models import inventory,mobilestock


class inventorySerializers(serializers.ModelSerializer):
    class Meta:
        model=inventory
        fields=['branch_code','model','mobile','quantity']

class mobilestockSerializers(serializers.ModelSerializer):
    class Meta:
        model=mobilestock
        fields=['mobile','model','price','quantity','amount']