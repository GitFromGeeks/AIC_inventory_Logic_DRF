from django.db import models


class credit(models.Model):
    branch_code=models.CharField(max_length=15)
    credit=models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    id=models.AutoField(primary_key=True)

    def __str__(self):
        return self.branch_code