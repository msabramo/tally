from __future__ import absolute_import

from collections import Callable, Sized, Iterable
from itertools import izip

from ..exceptions import UnimplementedException
from ..storage import get_storage


class Manager(object):
    """
    Base manager class for metrics. It should be responsible for dealing with
    a set of metrics of that type. Getting them all for example or performing
    operations to them all.
    """

    def __init__(self, storage=None):

        if storage:
            self.storage = storage
        else:
            self.storage = get_storage()


class Metric(Callable, Sized, Iterable):
    """
    Base metric class. Responsible for an individual metric and the actions
    that you can do with it.
    """

    def __init__(self, key, storage=None):

        if storage:
            self.storage = storage
        else:
            self.storage = get_storage()

        self.key = key

    def __iter__(self):
        return iter(self.keys())

    def __len__(self):
        return len(self.keys())

    def __call__(self):
        raise UnimplementedException("")

    def keys(self):
        raise UnimplementedException("")

    def timestamps(self):

        for key in self.keys():

            # split the key to get the timestamp part
            key = key.rsplit(":", 1)[1]
            # convert to int
            key = float(key)
            yield key

    def timestamp_items(self):
        return izip(self.timestamps(), self.values())

    def items(self):
        return izip(self.keys(), self.values())
