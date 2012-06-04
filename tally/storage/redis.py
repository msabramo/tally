from __future__ import absolute_import

from redis.connection import UnixDomainSocketConnection, Connection
from redis import ConnectionPool, Redis

from tally import conf
from tally.storage.base import BaseBackend
from tally.utils.functools import memoize


class CacheConnectionPool(object):
    _connection_pool = None

    def get_connection_pool(self, host='127.0.0.1', port=6379, db=1,
            password=None, unix_socket_path=None):

        if self._connection_pool is None:
            connection_class = (
                unix_socket_path and UnixDomainSocketConnection or Connection
            )
            kwargs = {
                'db': db,
                'password': password,
                'connection_class': connection_class,
            }
            if unix_socket_path is None:
                kwargs.update({
                    'host': host,
                    'port': port,
                })
            else:
                kwargs['path'] = unix_socket_path
            self._connection_pool = ConnectionPool(**kwargs)
        return self._connection_pool

pool = CacheConnectionPool()


METRIC_COUNTERS_KEY = "METRIC_COUNTERS_KEY"
METRIC_RECORDS_KEY = "METRIC_RECORDS_KEY"

_key_cache = {}


class RedisBackend(BaseBackend):

    def __init__(self, connection=None):

        if not connection:
            redis_db = conf.REDIS_DATABASE
            connection_pool = pool.get_connection_pool(db=redis_db)
            self.conn = Redis(connection_pool=connection_pool)
        else:
            self.conn = connection

    def store_key(self, key, set_key):
        """
        Stores the key in redis to keep a record of all the different metric
        keys that have been used. This is memoize's to reduce the number of
        add attempts to once per process launch.
        """

        def store(k1, k2):
            self.conn.sadd(k2, k1)
            return k1

        store = memoize(store, _key_cache, 2)

        return store(key, set_key)

    def store_counter(self, key):

        self.store_key(key, METRIC_COUNTERS_KEY)

    def store_record(self, key):

        self.store_key(key, METRIC_RECORDS_KEY)

    def counter_keychain(self, key):
        return self.conn.zrange(self.counter_keychain_key(key), 0, -1)

    def record_keychain(self, key):
        return self.conn.zrange(self.record_keychain_key(key), 0, -1)

    def counter_keychain_key(self, key):
        return self.keychain_key(key, "by.date")

    def record_keychain_key(self, key):
        return self.keychain_key(key, "stored.values")

    def incr(self, key):

        self.store_counter(key)

        value_key = self.value_key(key)
        keychain_key = self.counter_keychain_key(key)
        timestamp = self.timestamp()

        self.conn.incr(value_key)
        self.conn.zadd(keychain_key, value_key, timestamp)

    def record(self, key, value):

        self.store_record(key)

        value_key = self.value_key(key)
        keychain_key = self.record_keychain_key(key)
        timestamp = self.timestamp()

        self.conn.sadd(value_key, value)
        self.conn.zadd(keychain_key, value_key, timestamp)

    def counters(self):
        return self.conn.smembers(METRIC_COUNTERS_KEY)

    def records(self):
        return self.conn.smembers(METRIC_RECORDS_KEY)

    def counter_values(self, key):
        keys = self.counter_keychain(key)
        return self.conn.mget(keys)

    def record_values(self, key):
        keys = self.record_keychain(key)
        return self.conn.mget(keys)
