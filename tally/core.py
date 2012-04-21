from __future__ import absolute_import
from datetime import datetime, timedelta
from itertools import izip


from . import conf


class BaseAnalytics(object):

    def __init__(self, storage):

        self.storage = storage

    def incr(self, stat_name):
        self.storage.incr(stat_name)

    def generate_key(self, stat_name, account=None, date_instance=None):
        """
        Create a unique key for an individual stat. This is is defined by;

        <stat_name>:<account>:<date>

        Stat name could be "tags", account is the username, and date is the
        date that it was recorded for. This essentially then stores the count
        for each day and each account.

        date_instance is defaulted to today if not provided.
        """

        if not date_instance:
            date_instance = datetime.now()

        date_string = date_instance.strftime(conf.DATE_FORMAT)

        if not account:
            account = ''

        return "%s:%s:%s" % (stat_name, account, date_string)

    def generate_keys(self, stat_name, start_date, end_date, account=None):
        """
        Generate the keys to fetch data from Redis. This could alternatively
        have been done with the KEYS command and a pattern match, but this
        is much faster as it doesn't attempt pattern matching across the full
        Redis database
        """

        delta = end_date - start_date

        for i in range(delta.days + 1):

            date_instance = start_date + timedelta(days=i)

            yield self.generate_key(stat_name, account, date_instance)

    def fetch_values(self, keys, field=None):
        """
        Given a list of keys, fetch them all from Redis. This converts all the
        results to integers and replaced None results (for keys with no data)
        with 0.

        This is a helper method, to squash down the keys into values that can
        be summed and calculated in a few places. Therefore, it handles
        working with based keys and hashes.
        """

        def int_convert(l):
            for value in l:
                if value is None:
                    yield 0
                else:
                    yield int(value)

        data = []
        for key in keys:
            if field or self.conn.type(key) == "hash":
                if field:
                    data.append(self.conn.hget(key, field))
                else:
                    data.append(sum(int_convert(self.conn.hvals(key))))
            else:
                data.append(self.conn.get(key))

        return int_convert(data)

    def fetch_hash(self, keys):
        """
        Return a dictionary for each hash found.
        """
        for key in keys:
            yield key, self.conn.hgetall(key)

    def sum(self, stat_name, start_date, end_date, account=None, field=None):
        """
        Returns the sum of a set of fetched results.
        """

        keys = self.generate_keys(stat_name, start_date, end_date, account)
        return sum(self.fetch_values(keys, field))

    def flat_list(self, stat_name, start_date, end_date, account=None, field=None):
        """
        Return a list of 2-tuples that contains the key and numberic values.
        The key is left as a flat string.
        """

        # Convert to a list as we want to use it twice.
        keys = list(self.generate_keys(stat_name, start_date, end_date, account))
        return izip(keys, self.fetch_values(keys, field))