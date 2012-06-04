from unittest2 import TestCase
from mock import patch


class RedisBackendTestCase(TestCase):

    def setUp(self):

        from tally.storage.base import BaseBackend
        self.backend = BaseBackend()

    @patch("tally.storage.base.now", return_value=1338810332.18)
    def test_value_key(self, *args):
        self.assertEqual("my_key:by.date:1338810332.18", self.backend.value_key("my_key"))

    def test_keychain_key(self):
        self.assertEqual("my_key:by.date:keys", self.backend.keychain_key("my_key", "by.date"))
