# Generated by Django 3.0.4 on 2020-03-27 19:30

import Person.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('AadharCardNo', models.CharField(max_length=16, primary_key=True, serialize=False, unique=True, verbose_name='Aadhar Card No')),
                ('AadharCardF', models.ImageField(upload_to=Person.models.uploadAdharFront, verbose_name='Aadhar Card Front')),
                ('AadharCardB', models.ImageField(upload_to=Person.models.uploadAdharBack, verbose_name='Aadhar Card Back')),
                ('recentPicture', models.ImageField(upload_to=Person.models.uploadProfilePicture, verbose_name='Profile Picture')),
                ('firstName', models.CharField(help_text='It Include Both First Name and Middle Name(if required)', max_length=120, verbose_name='First Name')),
                ('lastName', models.CharField(help_text='It Include Last Name', max_length=50, verbose_name='Last Name')),
                ('Addr', models.TextField(help_text='Provided is the Start Of Emergency Outing', verbose_name='From Address')),
                ('phoneNumber', models.CharField(max_length=10, verbose_name='Phone Number')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'Person',
                'verbose_name_plural': 'Persons',
            },
        ),
    ]