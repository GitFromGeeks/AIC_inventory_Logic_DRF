from django.db import models


class accinventory(models.Model):
    id=models.AutoField(primary_key=True)
    branch_code=models.CharField(max_length=15)
    acc_name=models.CharField(max_length=200)
    quantity=models.IntegerField()

    def __str__(self):
        return self.acc_name


class accstock(models.Model):
    acc_name=models.CharField(max_length=200)
    price=models.IntegerField()
    quantity=models.IntegerField()
    amount=models.IntegerField()

    def __str__(self):
        return self.acc_name