from django.db import models

# Create your models here.
class WorkerDetails(models.Model):

    id              = models.AutoField(primary_key=True)

    name            = models.CharField(max_length=30)

    mobileNumber    = models.BigIntegerField()

    username        = models.CharField(max_length=10,unique=True)

    password        = models.CharField(max_length=256)

    worktype        = models.CharField(max_length=30,null=True)

    isActivated     = models.BooleanField(null=True)

    accessToken     = models.CharField(max_length=256)

    createdOn       = models.DateField()


    # def __str__(self):
    #     return self