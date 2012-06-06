from __future__ import absolute_import

from functools import wraps
from time import time

from .base import Manager, Metric


class RecordManager(Manager):

    def add(self, key, value):
        self.storage.record(key, value)

    def __call__(self, key):

        def inner_timer(f):

            @wraps(f)
            def wrapper(*args, **kwds):
                t = time()
                result = f(*args, **kwds)
                v = time() - t
                print v
                self.add(key, v)
                return result

            return wrapper

        return inner_timer

    def values(self, key):
        return self.storage.record_values(key)

    def keys(self):
        return self.storage.records()

    def get(self, key):
        return RecordMetric(storage=self.storage, key=key)


class RecordMetric(Metric):

    def add(self, value):
        self.storage.record(self.key, value)

    def __call__(self, fn=None):

        def inner_timer(f):

            @wraps(f)
            def wrapper(*args, **kwds):
                t = time()
                result = f(*args, **kwds)
                self.add(time() - t)
                return result

            return wrapper

        if fn:
            return inner_timer(fn)

        return inner_timer

    def values(self):
        return self.storage.record_values(self.key)

    def keys(self):
        return self.storage.record_keychain(self.key)

    def min(self):
        return min(min(s) for s in self.values())

    def max(self):
        return max(max(s) for s in self.values())
