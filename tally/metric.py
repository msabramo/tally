from __future__ import absolute_import

from . import conf
from .core import BaseAnalytics
from .util import import_module


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
