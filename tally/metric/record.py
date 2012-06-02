from __future__ import absolute_import

from functools import wraps
from time import time

from .base import Manager, Metric


class BaseRecord(object):

    def add(self, key, value):
        self.storage.record(key, value)

    def __call__(self, key):

        def inner_timer(f):

            @wraps(f)
            def wrapper(*args, **kwds):
                t = time()
                result = f(*args, **kwds)
                self.add(key, time() - t)
                return result

            return wrapper

        return inner_timer


class RecordManager(BaseRecord, Manager):

    def add(self, key, value):
        super(RecordManager, self).add(key, value)

    def __call__(self, key):
        super(RecordManager, self).__call__(key)

    def values(self, key):
        return self.storage.record_values(key)

    def keys(self):
        return self.storage.records()

    def get(self, key):
        return RecordMetric(storage=self.storage, key=key)


class RecordMetric(BaseRecord, Metric):

    def add(self, value):
        super(RecordMetric, self).add(self.key, value)

    def __call__(self):
        super(RecordMetric, self).__call__(self.key)

    def values(self):
        return self.storage.record_values(self.key)

    def keys(self):
        return self.storage.record_keyring(self.key)
