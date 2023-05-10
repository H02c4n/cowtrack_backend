from django.db import models

# Create your models here.


class Cow(models.Model):
    cow_Id = models.PositiveSmallIntegerField()
    cow_birthday = models.DateField(auto_created=False)



class Vaccine(models.Model):
    cow_Id = models.ForeignKey(Cow, on_delete=models.CASCADE)
    trikofiti_status_1D = models.BooleanField(blank=True, null=True)
    trikofiti_status_14D = models.BooleanField(blank=True, null=True)
    brd_clostridial_status_17D = models.BooleanField(blank=True, null=True)
    brd_clostridial_status_45D = models.BooleanField(blank=True, null=True)
    sap_status_2M = models.BooleanField(blank=True, null=True)
    sap_status_3M = models.BooleanField(blank=True, null=True)
    brucella_status_3M = models.BooleanField(blank=True, null=True)
    lsd_status_4M = models.BooleanField(blank=True, null=True)
    lsd_status_5M = models.BooleanField(blank=True, null=True)
    brucella_status_7M = models.BooleanField(blank=True, null=True)
    brd_clostridial_status_8M = models.BooleanField(blank=True, null=True)
    sap_status_9M = models.BooleanField(blank=True, null=True)
    bvd_ibr_status_12M = models.BooleanField(blank=True, null=True)
    bvd_ibr_status_13M = models.BooleanField(blank=True, null=True)
    sap_status_15M = models.BooleanField(blank=True, null=True)
    lsd_status_17M = models.BooleanField(blank=True, null=True)
    clostridial_status_20M = models.BooleanField(blank=True, null=True)
    sap_status_21M = models.BooleanField(blank=True, null=True)
