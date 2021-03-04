from django.db import models

class stockinfo(models.Model):
    branch_code=models.CharField(max_length=15)
    imei=models.CharField(max_length=30)
    mobile=models.CharField(max_length=100)

    created_at=models.DateField(auto_now_add=True)
    id=models.AutoField(primary_key=True)

    def __str__(self):
        return self.mobile