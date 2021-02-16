from django.db import models


class myprofile(models.Model):
    branch_code=models.CharField(max_length=15)
    franchise_plane=models.CharField(max_length=10)
    name=models.CharField(max_length=25)
    email=models.EmailField()
    phone_number=models.BigIntegerField()
    password=models.CharField(max_length=30)
    bank_name=models.CharField(max_length=100)
    acc_number=models.BigIntegerField()
    ifsc_code=models.CharField(max_length=15)
    profile_photo=models.ImageField()
    shop_add=models.CharField(max_length=250)
    home_add=models.CharField(max_length=250)
    aadhaar_number=models.BigIntegerField()
    pan_number=models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
