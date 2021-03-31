from django.db import models

class ledgers(models.Model):
    branch_code=models.CharField(max_length=15)
    mobile=models.CharField(max_length=150)
    model=models.CharField(max_length=30)
    price=models.BigIntegerField()
    quantity=models.IntegerField()
    credit=models.BigIntegerField()
    debit=models.BigIntegerField()


    created_at=models.DateField(auto_now_add=True)
    id=models.AutoField(primary_key=True)

class account(models.Model):
    id=models.AutoField(primary_key=True)
    created_at=models.DateField(auto_now_add=True)
    branch_code=models.CharField(max_length=15)
    aicout=models.BigIntegerField(default=0)
    aicin=models.BigIntegerField(default=0)
    description=models.CharField(max_length=100)

class debit(models.Model):
    branch_code=models.CharField(max_length=15)
    debit=models.BigIntegerField()

class debth(models.Model):
    branch_code=models.CharField(max_length=15)
    debth=models.BigIntegerField()