from rest_framework import serializers
from .models import ledgers,debth,account,debit



class debthSerializers(serializers.ModelSerializer):
    class Meta:
        model=debth
        fields=['branch_code','debth']

class debitSerializers(serializers.ModelSerializer):
    class Meta:
        model=debit
        fields=['branch_code','debit']


class ledgersSerializers(serializers.ModelSerializer):
    class Meta:
        model=ledgers
        fields=['created_at','branch_code','mobile','model','quantity','price','credit','debit']

class accountSerializers(serializers.ModelSerializer):
    class Meta:
        model=account
        fields=['id','created_at','branch_code','aicin','aicout','description']