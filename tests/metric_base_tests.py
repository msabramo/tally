from unittest2 import TestCase
from mock import Mock


class BaseMetricTestCase(TestCase):

    def setUp(self):

        from tally.metric.base import Metric

        self.mock_storage = Mock()
        self.metric = Metric("KEY", self.mock_storage)

    def test_metric_init(self):

        self.metric.timestamps()

        self.assertTrue(self.mock_storage.keys.called)
