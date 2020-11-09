# Generated by Django 3.0.4 on 2020-03-28 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pass', '0005_passapplication_valid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passapplication',
            name='acc',
            field=models.CharField(blank=True, choices=[('New', 'New Applicant'), ('Fake', 'Fake Applicant'), ('Old', 'Old Applicant')], default='New', max_length=50, verbose_name='Account Type'),
        ),
    ]
