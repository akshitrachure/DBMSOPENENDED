# Generated by Django 2.2.3 on 2020-04-09 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='payment',
            fields=[
                ('card_no', models.CharField(max_length=17, primary_key=True, serialize=False, verbose_name='Card_no')),
                ('name_of_card_holder', models.CharField(max_length=20, null=True, verbose_name='Name')),
                ('expiry_month', models.IntegerField(default=0, verbose_name='month')),
                ('expiry_year', models.IntegerField(default=0, verbose_name='Year')),
                ('confirm', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='trainDetails',
            fields=[
                ('train_no', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='train_no')),
                ('train_name', models.CharField(max_length=20, null=True, verbose_name='train_name')),
                ('From', models.CharField(max_length=20, null=True, verbose_name='from')),
                ('to', models.CharField(max_length=20, null=True, verbose_name='To')),
                ('arrival_time', models.TimeField(null=True)),
                ('departure_time', models.TimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='passenger',
            fields=[
                ('name', models.CharField(max_length=20, verbose_name='name')),
                ('username', models.CharField(max_length=30, primary_key=True, serialize=False, verbose_name='username')),
                ('email', models.EmailField(blank=True, max_length=70, verbose_name='email')),
                ('password', models.CharField(max_length=25, verbose_name='password')),
                ('phone', models.CharField(max_length=20, verbose_name='Phone')),
            ],
            options={
                'unique_together': {('email', 'phone')},
            },
        ),
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('train_name', models.CharField(max_length=20)),
                ('journey_date', models.DateField(null=True)),
                ('From', models.CharField(max_length=20, verbose_name='From')),
                ('to', models.CharField(max_length=20, verbose_name='To')),
                ('phone', models.CharField(max_length=20, verbose_name='Phone')),
                ('name', models.CharField(max_length=20, verbose_name='name')),
                ('nationality', models.CharField(max_length=20, verbose_name='Nationality')),
                ('gender', models.CharField(max_length=15, verbose_name='Gender')),
                ('age', models.IntegerField(default=15, null=True, verbose_name='Age')),
                ('choice_of_berth', models.CharField(choices=[('Lower', 'lower'), ('Middle', 'middle'), ('Upper', 'upper')], default='lower', max_length=10, null=True, verbose_name='Choice of Berth')),
                ('train_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.trainDetails')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.passenger')),
            ],
            options={
                'unique_together': {('username', 'train_no', 'journey_date')},
            },
        ),
    ]
