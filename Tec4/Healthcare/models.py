from django.db import models


# Create your models here.


class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)


class Request(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    patientId = models.ForeignKey(to='Patient', on_delete=models.CASCADE)
