from mock import MagicMock
from unittest2 import TestCase


class CounterMetricTestCase(TestCase):

    def setUp(self):

        from tally.metric.counter import CounterMetric

        self.mock_storage = MagicMock()
        self.mock_storage.counter_keychain = MagicMock(return_value=['a:100', 'b:200', 'c:300'])

        self.metric = CounterMetric("KEY", storage=self.mock_storage)

    def test_iter(self):

        self.assertEqual(['a:100', 'b:200', 'c:300'], [k for k in self.metric])

    def test_metric_timestamps(self):

        result = list(self.metric.timestamps())

        self.assertTrue(self.mock_storage.counter_keychain.called)
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


class CounterManagerTestCase(TestCase):

    def setUp(self):

        from tally.metric.counter import CounterManager

        self.mock_storage = MagicMock()
        self.mock_storage.counter_keychain = MagicMock(return_value=['a:100', 'b:200', 'c:300'])

        self.manager = CounterManager(storage=self.mock_storage)

    def test_decorator_interface(self):

        @self.manager("registrations")
        def register_user():
            pass

        register_user()
