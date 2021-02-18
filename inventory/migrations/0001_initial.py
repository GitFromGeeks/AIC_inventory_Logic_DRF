# Generated by Django 3.1.6 on 2021-02-16 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='inventory',
            fields=[
                ('branch_code', models.CharField(max_length=15)),
                ('model', models.CharField(max_length=40)),
                ('mobile', models.CharField(max_length=200)),
                ('quantity', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]