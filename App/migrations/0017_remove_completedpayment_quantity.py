# Generated by Django 4.2.6 on 2024-01-05 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0016_productorder'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='completedpayment',
            name='quantity',
        ),
    ]
