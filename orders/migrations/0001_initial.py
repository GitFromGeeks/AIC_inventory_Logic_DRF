# Generated by Django 3.1.6 on 2021-02-15 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='orders',
            fields=[
                ('branch_code', models.CharField(max_length=15)),
                ('model', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=200)),
                ('price', models.IntegerField(max_length=20)),
                ('quantity', models.IntegerField(max_length=5)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
    ]