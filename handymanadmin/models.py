from django.db import models

# Create your models here.
class HandymanAdminDetails(models.Model):

    id              = models.AutoField(primary_key=True,unique=True)

    name            = models.CharField(max_length=30)

    mobileNumber    = models.CharField(max_length=10,unique=True)

    username        = models.CharField(max_length=10,unique=True)

    password        = models.CharField(max_length=500)

    accessToken     = models.CharField(max_length=500)

    createdOn       = models.DateField()

