from rest_framework import serializers
from .models import stockinfo


class stockinfoSerializers(serializers.ModelSerializer):
    class Meta:
        model=stockinfo
        fields=['created_at','branch_code','imei','mobile']