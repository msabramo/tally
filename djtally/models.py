from django.db import models


class Record(models.Models):
    name = models.CharField()


class RecordValue(models.Model):
    date = models.DateTimeField()
    value = models.IntegerField()


class Counter(models.Models):
    name = models.CharField()


class CounterValue(models.Model):
    date = models.DateTimeField()
