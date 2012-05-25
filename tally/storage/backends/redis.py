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


METRIC_NAMES_KEY = "METRIC_NAMES_KEY"
METRIC_STORE_KEY = "METRIC_STORE_KEY"

_key_cache = {}


class Backend(BaseBackend):

    def __init__(self):

        redis_db = conf.REDIS_DATABASE
        connection_pool = pool.get_connection_pool(db=redis_db)
        self.conn = Redis(connection_pool=connection_pool)

    def store_key(self, key, set_key):

        def store(k1, k2):
            self.conn.sadd(k2, k1)
            return k1

        store = memoize(store, _key_cache, 2)

        return store(key, set_key)

    def incr(self, key):

        self.store_key(key, METRIC_NAMES_KEY)

        value_key = self.value_key(key)
        keyring_key = self.keyring_key(key, "by.date")
        timestamp = self.timestamp()

        self.conn.incr(value_key)
        self.conn.zadd(keyring_key, value_key, timestamp)

    def record(self, key, value):

        self.store_key(key, METRIC_STORE_KEY)

        value_key = self.value_key(key)
        keyring_key = self.keyring_key(key, "stored.values")
        timestamp = self.timestamp()

        self.conn.sadd(value_key, value)
        self.conn.zadd(keyring_key, value_key, timestamp)

    def counters(self):
        return self.conn.smembers(METRIC_NAMES_KEY)

    def records(self):
        return self.conn.smembers(METRIC_STORE_KEY)

    def keyring(self, key):
        return self.conn.zrange(self.keyring_key(key, "by.date"), 0, -1)

    def values(self, key):
        keys = self.keyring(key)
        return self.conn.mget(keys)
