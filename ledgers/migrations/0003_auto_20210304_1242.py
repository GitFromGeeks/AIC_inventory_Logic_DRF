# Generated by Django 3.1.6 on 2021-03-04 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ledgers', '0002_debth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ledgers',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]