# Generated by Django 4.2.6 on 2023-12-15 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0007_completedpayment_user_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='completedpayment',
            name='product_confirm',
        ),
        migrations.AddField(
            model_name='completedpayment',
            name='product_confirm',
            field=models.ManyToManyField(to='App.productcomfirm'),
        ),
    ]