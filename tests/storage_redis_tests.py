from unittest2 import TestCase
from mock import MagicMock, patch


class RedisBackendTestCase(TestCase):

    def setUp(self):
        from tally.storage.redis import RedisBackend
        self.mock_connection = MagicMock()
        self.backend = RedisBackend(connection=self.mock_connection)

    @patch("tally.storage.base.now", return_value=1338810332.18)
    def test_value_key(self, *args):
        self.assertEqual("my_key:by.date:1338810332.18", self.backend.value_key("by.date", "my_key"))

    def test_keychain_key(self):
        self.assertEqual("my_key:by.date:keys", self.backend.keychain_key("my_key", "by.date"))

    def test_store_counter(self):
        self.backend.store_counter("my_counter")
        self.mock_connection.sadd.assert_called_with('METRIC_COUNTERS_KEY', 'my_counter')

    def test_get_counter(self):
        self.mock_connection.smembers = MagicMock(return_value=["my_counter"])
        self.assertIn("my_counter", self.backend.counters())

    def test_store_record(self):
        self.backend.store_record("my_record")
        self.mock_connection.sadd.assert_called_with('METRIC_RECORDS_KEY', 'my_record')

    def test_get_record(self):
        self.mock_connection.smembers = MagicMock(return_value=["my_record"])
        self.assertIn("my_record", self.backend.records())

    def test_now(self):
        self.assertEqual(self.backend.timestamp().__class__, float)

    def test_incr(self):
        self.backend.timestamp = MagicMock(return_value=100000)

        self.backend.incr("my_thing")

        self.mock_connection.incr.assert_called_with('my_thing:by.date:100000')
        self.mock_connection.zadd.assert_called_with(
            'my_thing:by.date:keys', 'my_thing:by.date:100000', 100000)

    def test_record(self):
        self.backend.timestamp = MagicMock(return_value=100000)

        self.backend.record("my_key", 51)

        self.mock_connection.sadd.assert_called_with('my_key:stored.values:100000', 51)
        self.mock_connection.zadd.assert_called_with(
            'my_key:stored.values:keys', 'my_key:stored.values:100000', 100000)
