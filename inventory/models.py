from django.db import models


class inventory(models.Model):
    branch_code=models.CharField(max_length=15)
    model=models.CharField(max_length=40)
    mobile=models.CharField(max_length=200)
    quantity=models.IntegerField()

    def __str__(self):
        return self.branch_code