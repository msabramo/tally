from unittest2 import TestCase


class ReportTestCase(TestCase):

    def setUp(self):
        # should create dummy data or load a fixture?
        pass

    def test_sum(self):

        from tally.metric import report
        self.assertEqual(report("my_metric").sum(), 20)

    def test_min(self):

        from tally.metric import report
        self.assertEqual(report("my_metric").min(), 20)

    def test_max(self):

        from tally.metric import report
        self.assertEqual(report("my_metric").max(), 20)

    def test_date_filter(self):
        from tally.metric import report

        r = report("my_metric", start=self.two_months_ago, end=self.today)

        #assert?
