# Generated by Django 3.0.4 on 2020-03-27 19:30

import Pass.models
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PassApplication',
            fields=[
                ('ApplicationID', models.UUIDField(default=uuid.uuid4, help_text='This is a auto generated Application', primary_key=True, serialize=False, unique=True, verbose_name='Applicantion ID')),
                ('AadharCardNo', models.CharField(max_length=16, verbose_name='Aadhar Card No')),
                ('AadharCardF', models.ImageField(upload_to=Pass.models.uploadAdharFront, verbose_name='Aadhar Card Front')),
                ('AadharCardB', models.ImageField(upload_to=Pass.models.uploadAdharBack, verbose_name='Aadhar Card Back')),
                ('recentPicture', models.ImageField(upload_to=Pass.models.uploadProfilePicture, verbose_name='Profile Picture')),
                ('firstName', models.CharField(help_text='It Include Both First Name and Middle Name(if required)', max_length=120, verbose_name='First Name')),
                ('lastName', models.CharField(help_text='It Include Last Name', max_length=50, verbose_name='Last Name')),
                ('fromAddr', models.TextField(help_text='Provided is the Start Of Emergency Outing', verbose_name='From Address')),
                ('destination', models.TextField(help_text='Provided is the End Destiantion of the Outing', verbose_name='Destination')),
                ('purpose', models.TextField(verbose_name='Purpose Of Outing')),
                ('hourRequested', models.IntegerField(help_text='Maximum to 3hr Allowed or can reduce if required', verbose_name='Hours Requested')),
                ('when', models.DateTimeField(auto_now_add=True, verbose_name='Applied when')),
                ('phoneNumber', models.CharField(max_length=10, verbose_name='Phone Number')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('acc', models.CharField(blank=True, choices=[('New', 'New Applicant'), ('Fake', 'Fake Applicant'), ('Old', 'Old Applicant')], default='Old', max_length=50, verbose_name='Account Type')),
                ('fastFill', models.BooleanField(default=False, help_text='Is Fast Fill ID is Used', verbose_name='Fast Fill ID')),
                ('status', models.CharField(choices=[('Not', 'Not Seen'), ('Reject', 'Rejected'), ('Held', 'With Held'), ('Approve', 'Approved')], max_length=50, verbose_name='Status Of Application')),
                ('response', models.BooleanField(default=False, help_text='E pass is send or not', verbose_name='Response Send')),
                ('when_passed', models.DateTimeField(blank=True, null=True, verbose_name='When passed')),
            ],
            options={
                'verbose_name': 'Pass Application',
                'verbose_name_plural': 'Pass Applications',
            },
        ),
    ]