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
