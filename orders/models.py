from django.db import models

class orders(models.Model):
    branch_code=models.CharField(max_length=15)
    model=models.CharField(max_length=50)
    mobile=models.CharField(max_length=200)
    price=models.IntegerField()
    quantity=models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    id=models.AutoField(primary_key=True)

    def __str__(self):
        return self.branch_code