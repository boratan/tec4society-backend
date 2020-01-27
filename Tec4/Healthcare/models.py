from django.db import models


# Create your models here.


class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)


class Municipality(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)


class Hospital(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)


class Supplier(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)


class Request(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    patientId = models.ForeignKey(to='Patient', on_delete=models.CASCADE)
    hospitalId = models.ForeignKey(to='Hospital', on_delete=models.CASCADE)
    hospitalAgree = models.IntegerField(choices=((1, "Approved"),
                                                 (2, "Disapproved"),
                                                 (3, "Pending")),
                                        default=1)
    municipalityId = models.ForeignKey(to='Municipality', on_delete=models.CASCADE)
    municipalityAgree = models.IntegerField(choices=((1, "Approved"),
                                                     (2, "Disapproved"),
                                                     (3, "Pending")),
                                            default=1)
    supplierId = models.ForeignKey(to='Supplier', on_delete=models.CASCADE)
    supplierAgree = models.IntegerField(choices=((1, "Approved"),
                                                 (2, "Disapproved"),
                                                 (3, "Pending")),
                                        default=1)
