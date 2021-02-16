from rest_framework import serializers
from .models import credit


class creditSerializers(serializers.ModelSerializer):
    class Meta:
        model=credit
        fields=['id','created_at','branch_code','credit']