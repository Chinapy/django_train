from django.db import models


class SampleModel(models.model):
    title = models.CharField(max_length=100)
    number= models.IntegerField()
# Create your models here.
