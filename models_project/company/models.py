from django.db import models

# Create your models here.


class Employee(models.Model):
    idNumber = models.CharField(max_length=10, blank=False, null=False)
    firstName = models.CharField(max_length=30, blank=False, null=False)
    lastName = models.CharField(max_length=30, blank=False, null=False)
    email = models.CharField(max_length=30, blank=False, null=False)
    address = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        self.firstName


class Job(models.Model):
    title = models.CharField(max_length=15, blank=False, null=False)
    description = models.TextField(null=True)

    def __str__(self):
        self.title


class Salary(models.Model):
    amount = models.IntegerField(null=False, blank=False)
    extraDec = models.BooleanField(default=False)
    extraJun = models.BooleanField(default=False)

    def __str__(self):
        self.amount


class Place(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    address = models.CharField(max_length=50, null=False, blank=False)
    zipCode = models.CharField(max_length=5, null=False, blank=False)

    def __str__(self):
        self.name


class Location(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        self.name


class Country(models.model):
    name = models.CharField(max_length=30, null=False, blank=False)
    country_code = models.CharField(max_length=6, blank=False, null=False)

    def __str__(self):
        self.name
