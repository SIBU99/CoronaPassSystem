# Generated by Django 3.0.4 on 2020-03-31 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pass', '0009_auto_20200329_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='passapplication',
            name='block',
            field=models.CharField(blank=True, max_length=60, verbose_name='Applying Block'),
        ),
    ]
