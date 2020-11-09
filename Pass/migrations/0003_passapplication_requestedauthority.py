# Generated by Django 3.0.4 on 2020-03-28 04:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Authority', '0001_initial'),
        ('Pass', '0002_auto_20200328_0126'),
    ]

    operations = [
        migrations.AddField(
            model_name='passapplication',
            name='requestedAuthority',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='AuthorityApplications', to='Authority.Authorizer', verbose_name='Requested Authority'),
            preserve_default=False,
        ),
    ]