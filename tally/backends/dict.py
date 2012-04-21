"""
A dict storage backend, that simple stores the values in a dict using Pythons
built in datastructures.

WARNING. This should not be used for anything real, its created simply for
testing, development and debugging purposes.

"""

from __future__ import absolute_import

from datetime import date

from . import BaseBackend


def today():
    return date.today()


class Backend(BaseBackend):

    store = None

    def __init__(self):
        if self.store is None:
            self.store = {}

    def incr(self, key):

        value_key = self.value_key(key)
        keys_key = self.keys_key(key)

        self.store[value_key] = self.store.get(value_key, 0) + 1

        self.store[keys_key] = self.store.get(keys_key, set())
        self.store[keys_key].add(value_key)

    def get(self, key):
        return self.store.get(self.value_key(key))

    def flush(self):
        Backend.store = {}
