# Generated by Django 4.0.3 on 2022-04-14 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_productinorder_session_key'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productinorder',
            old_name='nmb',
            new_name='num',
        ),
    ]
