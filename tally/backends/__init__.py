from __future__ import absolute_import

from datetime import date

from .. import conf


def today():
    return date.today()


class BaseBackend(object):

    def date_string(self):
        date_instance = today()
        date_string = date_instance.strftime(conf.DATE_FORMAT)
        return date_string

    def value_key(self, key):
        key = "%s:by.date:%s" % (key, self.date_string())
        return key

    def keyring_key(self, key):
        key = "%s:by.date:keys" % key
        return key
