# Generated by Django 4.2.6 on 2023-12-15 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_alter_productcomfirm_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcomfirm',
            name='total_price',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='CompletedPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('S', 'Success'), ('F', 'Fail')], default='F', max_length=1)),
                ('booking_confirm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.bookingcomfirm')),
                ('product_confirm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.productcomfirm')),
            ],
        ),
    ]