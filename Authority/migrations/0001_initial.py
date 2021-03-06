# Generated by Django 3.0.4 on 2020-03-27 20:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Authorizer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(max_length=50, verbose_name='District Name')),
                ('block', models.CharField(max_length=50, verbose_name='Block Name')),
                ('fullname', models.CharField(max_length=150, verbose_name='Authorizer Fullname')),
                ('designation', models.CharField(max_length=50, verbose_name='Designation')),
                ('workstation', models.CharField(max_length=200, verbose_name='Work station')),
                ('allowLimter', models.IntegerField(default=10, verbose_name='Allowed Person Limit')),
                ('when', models.DateTimeField(auto_now_add=True, verbose_name='When Created')),
                ('auth', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='UserAuthority', to=settings.AUTH_USER_MODEL, verbose_name='Authentication Account')),
            ],
            options={
                'verbose_name': 'Authorizer',
                'verbose_name_plural': 'Authorizers',
            },
        ),
    ]
