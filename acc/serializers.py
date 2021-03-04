from rest_framework import serializers
from .models import accessorie


class accSerializers(serializers.ModelSerializer):
    class Meta:
        model=accessorie
        fields=['acc_name','price']