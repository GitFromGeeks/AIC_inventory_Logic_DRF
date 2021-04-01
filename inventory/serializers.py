from rest_framework import serializers
from .models import inventory,mobilestock,transferstock


class inventorySerializers(serializers.ModelSerializer):
    class Meta:
        model=inventory
        fields=['branch_code','model','mobile','quantity']

class mobilestockSerializers(serializers.ModelSerializer):
    class Meta:
        model=mobilestock
        fields=['mobile','model','price','quantity','amount']

class transferstockSerializers(serializers.ModelSerializer):
    class Meta:
        model=transferstock
        fields=['id','created_at','frombranch','tobranch','model']