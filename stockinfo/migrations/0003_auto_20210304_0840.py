# Generated by Django 3.1.6 on 2021-03-04 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockinfo', '0002_auto_20210216_0507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockinfo',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]