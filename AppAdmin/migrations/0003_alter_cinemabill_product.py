# Generated by Django 4.2.6 on 2024-01-03 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppAdmin', '0002_alter_cinemabill_branch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cinemabill',
            name='product',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
