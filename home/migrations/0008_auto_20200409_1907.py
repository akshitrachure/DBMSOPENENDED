# Generated by Django 2.2.3 on 2020-04-09 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20200409_1819'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='payment',
            new_name='payment_details',
        ),
    ]
