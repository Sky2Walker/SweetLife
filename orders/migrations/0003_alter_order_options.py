# Generated by Django 4.0.3 on 2022-05-06 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_coupon_order_discount'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('-created',), 'verbose_name': 'Замовленя', 'verbose_name_plural': 'Замовленя'},
        ),
    ]