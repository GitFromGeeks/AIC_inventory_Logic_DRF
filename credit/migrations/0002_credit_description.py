# Generated by Django 3.1.6 on 2021-02-18 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='credit',
            name='description',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]