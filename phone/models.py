from django.db import models



class phone(models.Model):
    model=models.CharField(max_length=30)
    mobile=models.CharField(max_length=200)
    ram=models.IntegerField()
    storage=models.IntegerField()
    color=models.CharField(max_length=20)
    price=models.BigIntegerField()

    def __str__(self):
        return self.mobile