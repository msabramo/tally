from __future__ import absolute_import

from functools import wraps

from .base import Manager, Metric


class CounterManager(Manager):

    def incr(self, key):
        self.storage.incr(key)

    def __call__(self, key):

        def inner_timer(f):

            @wraps(f)
            def wrapper(*args, **kwds):
                result = f(*args, **kwds)
                self.incr(key)
                return result

            return wrapper

        return inner_timer

    def values(self, key):
        return self.storage.counter_values(key)

    def keys(self):
        return self.storage.counters()

    def get(self, key):
        return CounterMetric(key, storage=self.storage)


class CounterMetric(Metric):

    def incr(self):
        self.storage.incr(self.key)

    def __call__(self, fn=None):

        def inner_timer(f):

            @wraps(f)
            def wrapper(*args, **kwds):
                result = f(*args, **kwds)
                self.incr()
                return result

            return wrapper

        if fn:
            return inner_timer(fn)

        return inner_timer

    def values(self):
        return self.storage.counter_values(self.key)

    def keys(self):
        return self.storage.counter_keychain(self.key)
