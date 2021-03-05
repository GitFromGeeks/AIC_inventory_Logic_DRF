# Generated by Django 3.1.6 on 2021-03-04 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20210217_1032'),
    ]

    operations = [
        migrations.CreateModel(
            name='mobilestock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=40)),
                ('mobile', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('amount', models.IntegerField()),
            ],
        ),
    ]