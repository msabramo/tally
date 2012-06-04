from __future__ import absolute_import

from functools import wraps

from .base import Manager, Metric


class BaseCounter(object):

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


class CounterManager(BaseCounter, Manager):

    def incr(self, key):
        super(CounterManager, self).incr(key)

    def __call__(self, key):
        super(CounterManager, self).__call__(key)

    def values(self, key):
        return self.storage.counter_values(key)

    def keys(self):
        return self.storage.counters()

    def get(self, key):
        return CounterMetric(key, storage=self.storage)


class CounterMetric(BaseCounter, Metric):

    def incr(self):
        super(CounterMetric, self).incr(self.key)

    def __call__(self):
        super(CounterMetric, self).__call__(self.key)

    def values(self):
        return self.storage.counter_values(self.key)

    def keys(self):
        return self.storage.counter_keychain(self.key)
