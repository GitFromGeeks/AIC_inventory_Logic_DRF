from rest_framework import serializers
from .models import accinventory,accstock


class accinventorySerializers(serializers.ModelSerializer):
    class Meta:
        model=accinventory
        fields=['id','branch_code','acc_name','quantity']

class accstockSerializers(serializers.ModelSerializer):
    class Meta:
        model=accstock
        fields=['acc_name','price','quantity','amount']