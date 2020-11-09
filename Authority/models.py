from django.db import models
from django.contrib.auth.models import User
from json import dump, load

# Create your models here.
class Authorizer(models.Model):
    "This will hold the information of Authority"
    auth = models.OneToOneField(
        User, 
        verbose_name="Authentication Account", 
        on_delete=models.CASCADE,
        related_name = "UserAuthority"
    )
    district = models.CharField(
        verbose_name="District Name", 
        max_length=50
    )
    block = models.CharField(
        verbose_name="Block Name", 
        max_length=50
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
    allowLimter = models.IntegerField(
        verbose_name="Allowed Person Limit",
        default=10,
    )
    when = models.DateTimeField(
        verbose_name="When Created",  
        auto_now_add=True
    )
    typE = models.CharField(
        verbose_name="Type Of Account",
        choices=(
            ("DM", "District Magistate"),
            ("EM", "Executive Magistate"),
            ("HC", "Health Department"),
        ),
        default="EM",
        max_length=50)



    class Meta:
        verbose_name = "Authorizer"
        verbose_name_plural = "Authorizers"