# Generated by Django 3.1.6 on 2021-02-15 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sell',
            fields=[
                ('branch_code', models.CharField(max_length=15)),
                ('model', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=200)),
                ('customer_name', models.CharField(max_length=15)),
                ('customer_number', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]
