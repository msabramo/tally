from mock import MagicMock
from unittest2 import TestCase


class RecordMetricTestCase(TestCase):

    def setUp(self):

        from tally.metric.record import RecordMetric

        self.mock_storage = MagicMock()
        self.mock_storage.record_keychain = MagicMock(return_value=['a:100', 'b:200', 'c:300'])

        self.metric = RecordMetric("KEY", storage=self.mock_storage)

    def test_iter(self):

        self.assertEqual(['a:100', 'b:200', 'c:300'], [k for k in self.metric])

    def test_metric_timestamps(self):

        result = list(self.metric.timestamps())

        self.assertTrue(self.mock_storage.record_keychain.called)
        self.assertEqual(result, [100.0, 200.0, 300.0])

    def test_decorator_interface(self):

        @self.metric()
        def count_me():
            pass

        count_me()
        count_me()

        @self.metric
        def count_me_too():
            pass

        count_me_too()
        count_me_too()


class RecordManagerTestCase(TestCase):

    def setUp(self):

        from tally.metric.record import RecordManager

        self.mock_storage = MagicMock()

        self.manager = RecordManager(storage=self.mock_storage)

    def test_decorator_interface(self):

        @self.manager("registrations")
        def register_user():
            pass

        register_user()
