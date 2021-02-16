from rest_framework import serializers
from .models import inventory


class inventorySerializers(serializers.ModelSerializer):
    class Meta:
        model=inventory
        fields=['branch_code','model','mobile','quantity']