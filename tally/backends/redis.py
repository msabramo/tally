from __future__ import absolute_import

from redis.connection import UnixDomainSocketConnection, Connection
from redis import ConnectionPool, Redis

from .. import conf
from . import BaseBackend


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


class Backend(BaseBackend):

    def __init__(self):
        redis_db = conf.REDIS_DATABASE

        connection_pool = pool.get_connection_pool(db=redis_db)

        self.conn = Redis(connection_pool=connection_pool)

    def incr(self, key):

        value_key = self.value_key(key)
        keyring_key = self.keyring_key(key)
        date_string = self.date_string()

        self.conn.incr(value_key)
        self.conn.zadd(keyring_key, value_key, date_string)
