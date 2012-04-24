from __future__ import absolute_import

from time import time


def now():
    """ This is abstracted here, primarily for mocking purposes """
    return time()


class BaseBackend(object):

    def timestamp(self):
        return now()

    def value_key(self, key):
        key = "%s:by.date:%s" % (key, self.timestamp())
        return key

    def keyring_key(self, key):
        key = "%s:by.date:keys" % key
        return key
