# Generated by Django 4.2.6 on 2024-01-03 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0014_completemoviepayment'),
        ('AppAdmin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cinemabill',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.branch'),
        ),
    ]