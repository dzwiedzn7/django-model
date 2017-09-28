from __future__ import unicode_literals
from django.db import models
#from django.contrib import admin


class Persons(models.Model):
    """docstring fo Persons"""
    first_name = models.CharField(max_lenght = 100)
    last_name = models.CharField(max_lenght = 100)
    date_of_birt = models.Date()
    GENDER_CHOICES = (('M','Male'),('F','FEMALE'))
    gender = models.CharField(max_lenght =1,choices = GENDER_CHOICES)


class Sensor(models.Model):
    """docstring fo Sensor"""
    name = models.CharField(max_lenght = 100)
    Desc= models.CharField(max_lenght = 1000)

class Series(models.Model):
    """docstring for Series"""
    pid = models.ForeignKey(Persons)
    sid = models.ForeignKey(Sensor)
    created = models.Data()
    last_mod = models.Date()


class Readings(models.Model):
    """docstring for Readings"""
    pid = models.ForeignKey(Persons)
    sid = models.ForeignKey(Sensor)
    srid = models.ForeignKey(Series)
    value =models.DecimalField(max_digits = 1)
    time_stamp = models.DecimalField(max_digits = 1)
#admin.site.register()
