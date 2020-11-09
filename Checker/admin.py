from django.contrib import admin
from .models import OnDuty, OnDutyChecked
# Register your models here.
admin.site.register(OnDuty)
admin.site.register(OnDutyChecked)