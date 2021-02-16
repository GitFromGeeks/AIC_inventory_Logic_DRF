from rest_framework import serializers
from .models import sell

class sellSerializers(serializers.ModelSerializer):
    class Meta:
        model=sell
        fields=['created_at','branch_code','customer_name','mobile','customer_number']