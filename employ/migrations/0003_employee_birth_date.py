# Generated by Django 3.2.9 on 2021-11-24 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employ', '0002_employee_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='birth_date',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
