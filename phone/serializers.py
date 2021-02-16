from rest_framework import serializers
from .models import phone



class phoneSerializers(serializers.ModelSerializer):
    class Meta:
        model=phone
        fields=['model','mobile','price']