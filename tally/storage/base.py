from __future__ import absolute_import

from time import time

from ..exceptions import UnimplementedException


def now():
    """
    This is abstracted here primarily for easy mocking
    """
    return time()


class BaseBackend(object):
    """
    Base reference class for backend classes.
    """

    def timestamp(self):
        return now()

    def value_key(self, key):
        key = "%s:by.date:%s" % (key, self.timestamp())
        return key

    def keychain_key(self, key, name):
        key = "%s:%s:keys" % (key, name)
        return key

    def incr(self, key):
        """
        Method should increment the given key name in the wrapped storage
        engine, keeping track of the datetime it was incremented.

        If this is the first time it has been tracked the counter should be
        set to 1 (thus starting at 0 and plus 1 for this)
        """
        raise UnimplementedException("Method not implemented by the backend")

    def record(self, key, value):
        """
        Method should store a value with a datetime against a key.
        """
        raise UnimplementedException("Method not implemented by the backend")

    def counters(self):
        """
        Method should return the names of all the counters.
        """
        raise UnimplementedException("Method not implemented by the backend")

    def records(self):
        """
        Method should return the names of all the records.
        """
        raise UnimplementedException("Method not implemented by the backend")

    def counter_values(self, key, start=None, end=None):
        """
        Return the stored datetime and values for a key, filtered by date
        ranges if given.
        """
        raise UnimplementedException("Method not implemented by the backend")

    def record_values(self, key, start=None, end=None):
        """
        Return the stored datetime and values for a key, filtered by date
        ranges if given.
        """
        raise UnimplementedException("Method not implemented by the backend")
