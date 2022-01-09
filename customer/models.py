from django.db import models

# Create your models here.

class CustomerDetails(models.Model):

    id              = models.AutoField(primary_key=True,unique=True)

    name            = models.CharField(max_length=30)

    mobileNumber    = models.BigIntegerField(unique=True)

    emailId         = models.EmailField(unique=True)

    username        = models.CharField(max_length=10,unique=True)

    password        = models.CharField(max_length=500)

    accessToken     = models.CharField(max_length=500)
    
    address         = models.CharField(max_length=30,null=True)

    pincode         = models.BigIntegerField(null=True)

    state           = models.CharField(max_length=30,null=True)

    city            = models.CharField(max_length=30,null=True)

