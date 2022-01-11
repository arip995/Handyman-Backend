from django.db import models

# Create your models here.
class HandymanAdminDetails(models.Model):

    id              = models.AutoField(primary_key=True,unique=True)

    name            = models.CharField(max_length=30)

    mobileNumber    = models.CharField(max_length=10,unique=True)

    username        = models.CharField(max_length=10,unique=True)

    password        = models.CharField(max_length=500)

    accessToken     = models.CharField(max_length=500)

    status          = models.BooleanField(null=True)

    branchId        = models.IntegerField(default=0)

    stateName       = models.CharField(max_length=30,default="")

    country         = models.CharField(max_length=30,default="INDIA")

    createdOn       = models.DateField()

