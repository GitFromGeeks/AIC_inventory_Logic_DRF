from rest_framework import serializers
from .models import ledgers,debth



class debthSerializers(serializers.ModelSerializer):
    class Meta:
        model=debth
        fields=['branch_code','debth']


class ledgersSerializers(serializers.ModelSerializer):
    class Meta:
        model=ledgers
        fields=['created_at','branch_code','mobile','model','quantity','price','credit','debit']