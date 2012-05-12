from __future__ import absolute_import


class BaseAnalytics(object):

    def __init__(self, storage):

        self.storage = storage

    def incr(self, stat_name):
        self.storage.incr(stat_name)

    def sum_keyring(self, keyring_name, start, end):
        pass

    def max_keyring(self, keyring_name, start, end):
        pass

    def min_keyring(self, keyring_name, start, end):
        pass

    def metric_keys(self):
        return self.storage.metric_keys()

    def value_keys(self, key):
        return self.storage.value_keys(key)

    def values(self, key):
        return self.storage.values(key)


class ImproperlyConfigured(Exception):
    pass
