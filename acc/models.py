from django.db import models

class accessorie(models.Model):
    acc_name=models.CharField(max_length=200)
    price=models.BigIntegerField()

    def __str__(self):
        return self.acc_name