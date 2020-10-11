# Generated by Django 3.0.7 on 2020-10-01 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20201001_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Delivered', 'Delivered'), ('OutForDelivery', 'OutForDelivery'), ('OutOfStock', 'OutOfStock')], max_length=100, null=True),
        ),
    ]