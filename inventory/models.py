from django.db import models


class inventory(models.Model):
    id=models.AutoField(primary_key=True)
    branch_code=models.CharField(max_length=15)
    model=models.CharField(max_length=40)
    mobile=models.CharField(max_length=200)
    quantity=models.IntegerField()

    def __str__(self):
        return self.branch_code


class mobilestock(models.Model):
    model=models.CharField(max_length=40)
    mobile=models.CharField(max_length=200)
    price=models.IntegerField()
    quantity=models.IntegerField()
    amount=models.IntegerField()

    def __str__(self):
        return self.mobile