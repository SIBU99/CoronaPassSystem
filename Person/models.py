from django.db import models

# Create your models here.
def uploadAdharFront(instance, filename):
    "this will upload the Aadhar Front Side"
    return f"{instance.AadharCardNo}/frontside/{filename}"

def uploadAdharBack(instance, filename):
    "this will upload the Aadhar Front Side"
    return f"{instance.AadharCardNo}/backside/{filename}"

def uploadProfilePicture(instance, filename):
    "this will upload the epass generated"
    return f"{instance.AadharCardNo}/RecentPicture/{filename}"
class Person(models.Model):
    "this will hold the information of the Person"
    AadharCardNo = models.CharField(
        verbose_name="Aadhar Card No", 
        max_length=16,
        unique=True,
        primary_key=True,
        blank=True
    )
    AadharCardF = models.ImageField(
        verbose_name="Aadhar Card Front", 
        upload_to=uploadAdharFront, 
        height_field=None, 
        width_field=None, 
        max_length=None
    )
    AadharCardB = models.ImageField(
        verbose_name="Aadhar Card Back", 
        upload_to=uploadAdharBack, 
        height_field=None, 
        width_field=None, 
        max_length=None
    ) 
    recentPicture = models.ImageField(
        verbose_name="Profile Picture", 
        upload_to=uploadProfilePicture, 
        height_field=None, 
        width_field=None, 
        max_length=None
    )
    firstName = models.CharField(
        verbose_name="First Name",
        help_text="It Include Both First Name and Middle Name(if required)",
        max_length=120
    )
    lastName = models.CharField(
        verbose_name="Last Name",
        help_text="It Include Last Name" ,
        max_length=50
    )
    Addr = models.TextField(
        verbose_name="From Address",
        help_text="Provided is the Start Of Emergency Outing"
    )
    phoneNumber = models.CharField(
        verbose_name="Phone Number", 
        max_length=10,
        unique=True
    )
    email = models.EmailField(
        verbose_name="Email", 
        max_length=254,
        blank=True,
        null=True
    )
    district = models.CharField(
        verbose_name="Applying District", 
        max_length=60
    )
    workstation = models.CharField(
        verbose_name="Workstation", 
        max_length=100
    )


    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "Persons"

