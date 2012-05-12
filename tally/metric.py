from __future__ import absolute_import

from tally import conf
from tally.core import BaseAnalytics
from tally.util import import_module


def importbackend(dotted_path):
    # This kinda sucks ATM.
    return import_module(dotted_path).Backend


def get_backend():
    backend_path = conf.STORAGE_BACKEND
    backend = importbackend(backend_path)
    return backend()


def get_analytics():
    backend = get_backend()
    return BaseAnalytics(backend)


def incr(key):
    a = get_analytics()
    a.incr(key)


def fetch_data(key):
    pass


def metric_keys():
    a = get_analytics()
    return a.metric_keys()


def value_keys(key):
    a = get_analytics()
    return a.value_keys(key)


def values(key):
    a = get_analytics()
    return a.values(key)
