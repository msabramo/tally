from datetime import datetime

from django.db import models


class Record(models.Models):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class RecordValue(models.Model):
    record = models.ForeignKey(Record)
    date = models.DateTimeField(default=datetime.now)
    value = models.IntegerField()


class Counter(models.Models):
    name = models.CharField(max_length=50)
    total = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name


class CounterValue(models.Model):
    counter = models.ForeignKey(Counter)
    date = models.DateTimeField(default=datetime.now)
