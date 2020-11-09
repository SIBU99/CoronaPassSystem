from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class OnDuty(models.Model):
    "this will hold the information of the OnDuty Checker Of this Pass"
    auth = models.OneToOneField(
        User, 
        verbose_name="Authentication Account", 
        on_delete=models.CASCADE,
        related_name = "UserOnDuty"
    )
    fullname = models.CharField(
        verbose_name="Authorizer Fullname", 
        max_length=150
    )
    designation = models.CharField(
        verbose_name="Designation", 
        max_length=50
    )
    workstation = models.CharField(
        verbose_name="Work station", 
        max_length=200
    )
    district = models.CharField(
        verbose_name="District Name", 
        max_length=50
    )
    block = models.CharField(
        verbose_name="Block Name", 
        max_length=50
    )
    phoneNumber = models.CharField(
        verbose_name="Phone Number", 
        max_length=10,
    )
    email = models.EmailField(
        verbose_name="Email", 
        max_length=254,
        blank=True,
        null=True
    )


    @property
    def checkedToday(self):
        "this will return the ID Checked"
        data = self.OnDutyCheckedPass.all().filter(
            date__day   = timezone.now().day,
            date__month = timezone.now().month,
            date__year  = timezone.now().year,
        )
        if data:
            data = data[0]
            return data.passIDChecked
        else:
            return None

    class Meta:
        verbose_name = "On Duty"
        verbose_name_plural = "On Dutys"

class OnDutyChecked(models.Model):
    "this will hold the information of the Person"
    checker = models.ForeignKey(
        OnDuty, 
        verbose_name="Checked Authority", 
        on_delete=models.CASCADE,
        related_name="OnDutyCheckedPass"
    )
    passIds = models.TextField(
        verbose_name="Enter the Pass Id",
        help_text="Note CSV Format",
        blank  = True,
        null = True,
    )
    date = models.DateField(
        "Date", 
        auto_now_add=True
    )

    @property
    def passIDChecked(self):
        "this will return the Pass Id Returned"
        if self.passIds:
            return self.passIds.split(",")
        else:
            return None


    class Meta:
        verbose_name = "On Duty Checked"
        verbose_name_plural = "On Duty Checkeds"
