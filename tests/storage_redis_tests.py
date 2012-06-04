from unittest2 import TestCase


class RedisBackendTestCase(TestCase):

    def setUp(self):
        from tally.storage.redis import RedisBackend
        self.backend = RedisBackend()
        self.redis = self.backend.conn
        self.redis.flushall()

    def test_store_counter(self):
        self.backend.store_counter("my_counter")
        self.assertIn("my_counter", self.backend.counters())

    def test_store_record(self):
        self.backend.store_record("my_record")
        self.assertIn("my_record", self.backend.records())

    def test_now(self):
        self.assertEqual(self.backend.timestamp().__class__, float)
