from django.db import models
from uuid import uuid4
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from Person.models import Person
from django.utils import timezone
from datetime import timedelta
import requests as req   
import json      


# Create your models here.
def uploadAdharFront(instance, filename):
    "this will upload the Aadhar Front Side"
    return f"{instance.AadharCardNo}/{instance.firstName.capitalize()} {instance.lastName.capitalize()}/frontside/{filename}"

def uploadAdharBack(instance, filename):
    "this will upload the Aadhar Front Side"
    return f"{instance.AadharCardNo}/{instance.firstName.capitalize() } { instance.lastName.capitalize()}/backside/{filename}"

def uploadProfilePicture(instance, filename):
    "this will upload the epass generated"
    return f"{instance.AadharCardNo}/{instance.firstName.capitalize()} { instance.lastName.capitalize()}/RecentPicture/{filename}"

def send_the_link(name, aadhar, phone_no):
    "this will send the otp using fast2sms api"
    url = "https://www.fast2sms.com/dev/bulk"
    #hide the api key
    key = "1zrRO4aB5F2spjYolkVqNtxAdJeZuHnhEDWMX9P3KS8UGIic7Q0Xo3yEaK1znpNJO8cdeSCGxFbMrALU"
    #key = os.environ.get("sms_api", None)
    querystring = dict()
    count = 3
    while count:
        querystring["authorization"] = key
        querystring["sender_id"]= "FSTSMS"
        querystring["language"]= "english"
        querystring["route"]="qt"
        querystring["numbers"] = f"{phone_no}"
        querystring["message"] = "25381"
        querystring["variables"] = "{CC}|{FF}"
        querystring["variables_values"] = f"{name}|{aadhar}"
    
        headers = {
        'cache-control': "no-cache"
        }
        count -= 1
        response = req.request("GET", url, headers=headers, params=querystring)
        if response.status_code == 200:
            print("Send the otp")
            return response.status_code
    else:
        print("Failed the otp")
        return response.status_code

class PassApplication(models.Model):
    "this will hold the information of the Applicant ID"
    ApplicationID = models.UUIDField(
        verbose_name="Applicantion ID",
        help_text = "This is a auto generated Application",
        primary_key = True,
        unique = True,
        default = uuid4
    )
    AadharCardNo = models.CharField(
        verbose_name="Aadhar Card No", 
        max_length=16,
        )
    AadharCardF = models.ImageField(
        verbose_name="Aadhar Card Front", 
        upload_to=uploadAdharFront, 
        height_field=None, 
        width_field=None, 
        max_length=None,
        blank=True,
        null = True,
    )
    AadharCardB = models.ImageField(
        verbose_name="Aadhar Card Back", 
        upload_to=uploadAdharBack, 
        height_field=None, 
        width_field=None, 
        max_length=None,
        blank=True,
        null = True,
    )
    recentPicture = models.ImageField(
        verbose_name="Profile Picture", 
        upload_to=uploadProfilePicture, 
        height_field=None, 
        width_field=None, 
        max_length=None,
        blank=True,
        null = True,
    )
    AadharCardFUrl = models.URLField(
        verbose_name="Adhar Card Front Url",
        max_length=200,
        blank=True,
        null = True,
    )
    AadharCardBUrl = models.URLField(
        verbose_name="Adhar Card Front Url",
        max_length=200,
        blank=True,
        null = True,
    )
    recentPictureUrl = models.URLField(
        verbose_name="Adhar Card Front Url",
        max_length=200,
        blank=True,
        null = True,
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
    fromAddr = models.TextField(
        verbose_name="From Address",
        help_text="Provided is the Start Of Emergency Outing"
    )
    destination = models.TextField(
        verbose_name="Destination",
        help_text="Provided is the End Destiantion of the Outing"
    )
    purpose = models.TextField(
        verbose_name="Purpose Of Outing"
    )
    hourRequested = models.IntegerField(
        verbose_name="Hours Requested",
        help_text="Maximum to 3hr Allowed or can reduce if required",
    )
    startTime = models.DateTimeField(
        verbose_name="Outing Start Time",  
    )
    when = models.DateTimeField(
        verbose_name="Applied when",  
        auto_now_add=True
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

    acc = models.CharField(
        verbose_name="Account Type", 
        max_length=50,
        choices=(
            ("New", "New Applicant"),
            ("Fake", "Fake Applicant"),
            ("Old", "Old Applicant")
        ),
        default="New",
        blank=True
    )
    district = models.CharField(
        verbose_name="Applying District", 
        max_length=60
    )
    block = models.CharField(
        verbose_name="Applying Block", 
        max_length=60,
        blank=True,
    )
    workstation = models.CharField(
        verbose_name="Workstation", 
        max_length=100
    )
    fastFill = models.BooleanField(
        verbose_name="Fast Fill ID",
        help_text="Is Fast Fill ID is Used",
        default=False
    )
    status = models.CharField(
        verbose_name="Status Of Application", 
        max_length=50,
        choices=(
            ("Not", "Not Seen"),
            ("Reject", "Rejected"),
            ("Held", "With Held"),
            ("Approve", "Approved")
        ),
        default="Not"
    )
    response = models.BooleanField(
        verbose_name="Response Send",
        help_text = "E pass is send or not",
        default=False
    )

    when_passed = models.DateTimeField(
        verbose_name="When passed", 
        blank=True,
        null=True
    )
    requestedAuthority = models.ForeignKey(
        "Authority.Authorizer", 
        verbose_name="Requested Authority", 
        on_delete=models.CASCADE,
        related_name="AuthorityApplications",
        blank=True,
    )
    valid = models.BooleanField(
        verbose_name="Vaild",
        help_text="The Validity of Pass",
        default=False,
    )
    endtdatetime =models.DateTimeField(
        verbose_name="Expiry of pass", 
        blank=True,
        null=True
    )

    @property
    def fullName(self):
        "this will return the fullName"
        return self.firstName+" "+self.lastName

    @property
    def applications(self):
        self.AuthorityApplications.all().order_by("-when")


    def clean(self):
        "this will validate the field"
        if  not self.phoneNumber.isdigit():
            raise ValidationError("Please Provide the Valid Phone Number")
        if not(self.hourRequested > 0 and self.hourRequested <= 3):
            raise ValidationError("Please Provide Requesting Outing Hour Less than 3 Hr")
        if not self.AadharCardNo.isdigit():
            raise ValidationError("Please Provide The Valid Aadhar Card Number")
    
    def save(self, *args, **kwargs):
        "This will triger when the save is called"
        self.block = self.requestedAuthority.block
        if self.fastFill:
            self.acc = "Old"
        else: 
            if self.acc != "Fake":
                self.acc = "New"
        if Person.objects.filter(AadharCardNo=self.AadharCardNo):
            self.acc="Old"
        
        if self.status == "Approve":
            self.when_passed = timezone.now()
            self.valid = True
            self.endtdatetime = self.startTime + timedelta(hours=self.hourRequested)
            
            self.response =True

        super(PassApplication, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Pass Application"
        verbose_name_plural = "Pass Applications"

@receiver(post_save, sender=PassApplication)
def Person_post_save_receiver(sender, instance, **kwargs):
    "This will save the Person Data"
    if instance.acc == "New":
        if not Person.objects.filter(AadharCardNo=instance.AadharCardNo):
            Person.objects.create(
                AadharCardNo = instance.AadharCardNo,
                AadharCardF = instance.AadharCardF,
                AadharCardB = instance.AadharCardB,
                firstName = instance.firstName,
                lastName = instance.lastName,
                Addr = instance.fromAddr,
                recentPicture = instance.recentPicture,
                phoneNumber = instance.phoneNumber,
                email = instance.email,
                district = instance.district,
                workstation = instance.workstation,
            )
    if instance.status == "Approve":
        payload = {
            "name":instance.firstName,
            "phone":instance.phoneNumber,
            "aadhar":instance.AadharCardNo,
        }
        url = f"http://kumarashirwradmishra.pythonanywhere.com/send/{payload['name']}/{payload['phone']}/{payload['aadhar']}"

        _ = req.get(url)