# Generated by Django 2.2.3 on 2020-04-09 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_payment_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='journey_date',
            field=models.CharField(default='01/01/2020', max_length=20, verbose_name='journey_date'),
        ),
    ]
