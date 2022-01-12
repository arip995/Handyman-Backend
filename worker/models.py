from django.db import models
from django.db.models.fields.json import JSONField
# from django.contrib.postgres.fields import JSONField
# from django.db.models.JSONField import


# Create your models here.
class WorkerDetails(models.Model):

    id                = models.AutoField(primary_key=True,unique=True)

    firstName         = models.CharField(max_length=30)

    lastName          = models.CharField(max_length=30)

    mobileNumber      = models.BigIntegerField(unique=True)

    username          = models.CharField(max_length=10,unique=True)

    password          = models.CharField(max_length=500)

    worktype          = models.CharField(max_length=30,null=True)

    isActivated       = models.BooleanField(null=True)

    accessToken       = models.CharField(max_length=500)

    createdOn         = models.DateField()


class WorkerInformation(models.Model):

    foreignId         = models.ForeignKey(WorkerDetails, on_delete=models.CASCADE)

    personalDetails   = JSONField(null=True)

    familyDetails     = JSONField(null=True)

    residenceDetails  = JSONField(null=True)

    workDetails       = JSONField(null=True)

    kyc               = JSONField(null=True)

    bankDetails       = JSONField(null=True)
