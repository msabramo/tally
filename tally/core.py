from __future__ import absolute_import

from tally import conf
from tally.utils import import_module


class BaseAnalytics(object):

    def __init__(self, storage):

        self.storage = storage

    def incr(self, stat_name):
        self.storage.incr(stat_name)

    def counters(self):
        return self.storage.counters()

    def records(self):
        return self.storage.records()

    def keyring(self, key):
        return self.storage.keyring(key)

    def values(self, key):
        return self.storage.values(key)

    def record(self, key, value):
        return self.storage.record(key, value)


class ImproperlyConfigured(Exception):
    pass


def importbackend(dotted_path):
    # TODO: Handle errors.
    return import_module(dotted_path).Backend


def get_backend():
    backend_path = conf.STORAGE_BACKEND
    backend = importbackend(backend_path)
    return backend()


def get_analytics():
    backend = get_backend()
    return BaseAnalytics(backend)


def fetch_data(key):
    pass
