from django.db import models

# Create your models here.
class WorkerDetails(models.Model):

    id              = models.AutoField(primary_key=True,unique=True)

    firstName       = models.CharField(max_length=30, default="")

    lastName        = models.CharField(max_length=30, default="")

    mobileNumber    = models.CharField(max_length=10,unique=True)

    username        = models.CharField(max_length=10,unique=True)

    password        = models.CharField(max_length=500)

    worktype        = models.CharField(max_length=30,null=True)

    isActivated     = models.BooleanField(null=True)

    accessToken     = models.CharField(max_length=500)

    createdOn       = models.DateField()


    # def __str__(self):
    #     return self