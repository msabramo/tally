"""
A set of Tally utility functions that provide shortcuts and the simplest API
access to features.
"""
from itertools import izip
from time import clock
from functools import wraps

from tally.core import get_analytics


def keys():
    """
    Return all of the stats that are currently stored in the backend.
    """
    a = get_analytics()
    return a.keys()


def values(key):
    """
    Return all of the values that are currently stored for keys in the backend.
    """
    a = get_analytics()
    return a.values(key)


def items(key):
    """
    Return a iterable of 2-tuples that contain the key and relevant value
    stored in the backend.
    """
    return izip(keys(), values())


def keyring(key):
    a = get_analytics()
    return a.keyring(key)


def incr(key):
    """
    Increment the value of a specific key.
    """
    a = get_analytics()
    a.incr(key)


def record(key, value=None):
    """
    record a specific value against a key.
    """

    a = get_analytics()
    a.record(key, value)

    return value


def counter(key):
    """
    Decorator factory to create a decorator that is bound to a key and will
    count the number of calls to the method it wraps
    """

    def inner_timer(f):

        @wraps(f)
        def wrapper(*args, **kwds):
            result = f(*args, **kwds)
            incr(key)
            return result

        return wrapper

    return inner_timer


def timer(key):
    """
    Decorator factory to create a decorator that is bound to a key and will
    record the execution time of what it wraps under that key.
    """

    def inner_timer(f):

        @wraps(f)
        def wrapper(*args, **kwds):
            t = clock()
            result = f(*args, **kwds)
            record(key, clock() - t)
            return result

        return wrapper

    return inner_timer
