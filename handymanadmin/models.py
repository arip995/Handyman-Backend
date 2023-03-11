from django.db import models

# Create your models here.
class HandymanAdminDetails(models.Model):

    id              = models.AutoField(primary_key=True,unique=True)

    name            = models.CharField(max_length=30)

    mobileNumber    = models.BigIntegerField(unique=True)

    username        = models.CharField(max_length=10,unique=True)

    password        = models.CharField(max_length=500)

    email           = models.CharField(max_length=50,unique=True,default="")

    accessToken     = models.CharField(max_length=500)

    status          = models.BooleanField(null=True)

    branchId        = models.IntegerField()

    stateName       = models.CharField(max_length=20)

    cityName       = models.CharField(max_length=20)

    country         = models.CharField(max_length=30,default="INDIA")

    createdOn       = models.DateField()

