from django.db import models

# Create your models here.

class CustomerDetails(models.Model):

    id              = models.AutoField(primary_key=True)

    name            = models.CharField(max_length=30)

    mobileNumber    = models.BigIntegerField()

    emailId         = models.EmailField()

    username        = models.CharField(max_length=10)

    password        = models.CharField(max_length=160)

    accessToken     = models.CharField(max_length=160)
    
    address         = models.CharField(max_length=30,null=True)

    pincode         = models.BigIntegerField(null=True)

    state           = models.CharField(max_length=30,null=True)

    city            = models.CharField(max_length=30,null=True)

