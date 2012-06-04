from django.db.models import F

from tally.storage.base import BaseBackend

from djtally.models import Counter, CounterValue, Report, ReportValue


class DjangoBackend(BaseBackend):

    def incr(self, key):
        c, _ = Counter.objects.get_or_create(name=key)
        CounterValue.objects.create(counter=c)
        Counter.objects.filter(key=key).update(count=F('count') + 1)

    def record(self, key, value):
        r, _ = Report.objects.get_or_create(name=key)
        ReportValue.objects.create(record=r, value=value)

    def counters(self):
        """
        Method should return the names of all the counters.
        """
        raise NotImplemented("Method not implemented by the backend")

    def records(self):
        """
        Method should return the names of all the records.
        """
        raise NotImplemented("Method not implemented by the backend")

    def counter_values(self, key, start=None, end=None):
        """
        Return the stored datetime and values for a key, filtered by date
        ranges if given.
        """
        raise NotImplemented("Method not implemented by the backend")

    def record_values(self, key, start=None, end=None):
        """
        Return the stored datetime and values for a key, filtered by date
        ranges if given.
        """
        raise NotImplemented("Method not implemented by the backend")
