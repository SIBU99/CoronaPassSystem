from django.db import models

# Create your models here.
class CheckUpRequest(models.Model):
    "this will hold the information of person requested for the checkup"
    fullName = models.CharField(
            verbose_name="Full Name",
            help_text="It Include The Full name OF The Person",
            max_length=120
        )
    symtoms = models.TextField(
            verbose_name="Sysmtoms Requested",
            help_text="Note CSV Format",
            blank  = True,
            null = True,
        )
    addr = models.TextField(
            verbose_name="Address",
            help_text="Address of the Person",
            blank  = True,
            null = True,
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


    district = models.CharField(
            verbose_name="Applying District", 
            max_length=60
        )
    block = models.CharField(
            verbose_name="Applying Block", 
            max_length=60
        )
    cityVillage = models.CharField(
            verbose_name="Applying City/Village", 
            max_length=60
        )

    when = models.DateTimeField(
            verbose_name="Applied when",  
            auto_now_add=True
        )
    status = models.CharField(
            verbose_name="Status Of Request", 
            max_length=50,
            choices=(
                ("Not", "Not Seen"),
                ("Pend", "Pending"),
                ("Checked", "Checked")
            ),
            default="Not"
        )
    checkedPerson = models.CharField(
            verbose_name="Checked Person",
            help_text="Checked Person",
            max_length=120,
            blank=True,
            null=True
        )
    send = models.BooleanField(
        verbose_name="Send",
        help_text="Team Send To Check",
        default=False,
    )

    

    class Meta:
        verbose_name = "CheckUpRequest"
        verbose_name_plural = "CheckUpRequests"