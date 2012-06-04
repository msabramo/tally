from unittest2 import TestCase
from mock import Mock


class BaseMetricTestCase(TestCase):

    def setUp(self):

        from tally.metric.counter import Counter

        self.mock_storage = Mock()
        self.metric = Counter("KEY", self.mock_storage)

    def test_metric_init(self):
        pass
