from unittest2 import TestCase


class RedisMetricTestCase(TestCase):

    def setUp(self):

        from tally.storage.redis import RedisBackend
        from tally.metric.counter import CounterMetric, CounterManager

        self.counter = CounterMetric()