from email.policy import default
from django.db import models
from django.db.models.fields.json import JSONField


# Create your models here.
class ProductDetails(models.Model):

    productId                      = models.AutoField(primary_key=True,unique=True)

    productShortDecription         = models.CharField(max_length=500,unique=True)

    productName                    = models.CharField(max_length=40,unique=True)

    price                          = models.IntegerField()

    totalTime                      = models.IntegerField()

    productCompleteDescription     = JSONField()

    productCategory                = models.CharField(max_length=20)