from mock import MagicMock
from unittest2 import TestCase


class BaseMetricTestCase(TestCase):

    def setUp(self):

        from tally.metric.base import Metric

        self.mock_storage = MagicMock()

        self.metric = Metric("KEY", storage=self.mock_storage)

    def test_metric_init(self):

        from tally.exceptions import UnimplementedException

        with self.assertRaises(UnimplementedException):
            list(self.metric.timestamps())


class BaseManagerTestCase(TestCase):

    def setUp(self):

        from tally.metric.base import Manager

        self.mock_storage = MagicMock()
        self.manager = Manager(storage=self.mock_storage)

    def test_manager_init(self):
        pass
