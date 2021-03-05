# Generated by Django 3.1.6 on 2021-03-04 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='accsell',
            fields=[
                ('branch_code', models.CharField(max_length=15)),
                ('acc_name', models.CharField(max_length=200)),
                ('customer_name', models.CharField(max_length=15)),
                ('customer_number', models.IntegerField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]