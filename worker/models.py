from django.db import models
from django.db.models.fields.json import JSONField
# from django.contrib.postgres.fields import JSONField
# from django.db.models.JSONField import


# Create your models here.
class WorkerDetails(models.Model):

    id                = models.AutoField(primary_key=True,unique=True)

    firstName         = models.CharField(max_length=30,null=True)

    lastName          = models.CharField(max_length=30,null=True)

    mobileNumber      = models.BigIntegerField(unique=True,null=True)

    username          = models.CharField(max_length=10,unique=True,null=True)

    password          = models.CharField(max_length=500,null=True)

    worktype          = models.CharField(max_length=30,null=True)

    isActivated       = models.BooleanField(null=True)

    accessToken       = models.CharField(max_length=500,null=True)

    createdOn         = models.DateField(null=True)


class WorkerInformation(models.Model):

    foreignId         = models.OneToOneField(WorkerDetails, on_delete=models.CASCADE,primary_key=True)

    # key               = models.IntegerField(unique=True)

    personalDetails   = JSONField(null=True)

    familyDetails     = JSONField(null=True)

    residenceDetails  = JSONField(null=True)

    workDetails       = JSONField(null=True)

    kyc               = JSONField(null=True)

    bankDetails       = JSONField(null=True)
