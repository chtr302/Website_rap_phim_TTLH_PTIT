# Generated by Django 4.2.6 on 2024-01-05 02:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0015_completedpayment_payment_date_and_more'),
        ('AppAdmin', '0004_cinemabill_payment_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='cinemastatistical',
            name='movie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='App.movie'),
        ),
        migrations.AddField(
            model_name='cinemastatistical',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AppAdmin.product'),
        ),
    ]
