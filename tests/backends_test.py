from unittest2 import TestCase


class DictBackendTestCase(TestCase):

    def setUp(self):
        from tally.storage.backends.dict import Backend
        self.storage = Backend()
        self.storage.flush()

    def test_incr(self):

        self.storage.incr("key")
        self.assertEqual(self.storage.get("key"), 1)

    def test_get_empty(self):

        result = self.storage.get("not-set")
        self.assertEqual(result, None)

    def test_get_value(self):

        self.storage.incr("key")
        self.assertEqual(self.storage.get("key"), 1)
