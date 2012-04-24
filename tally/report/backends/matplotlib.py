from __future__ import absolute_import

from tally.core import ImproperlyConfigured

try:
    import numpy
except ImportError:
    raise ImproperlyConfigured("Numpy is required to use the matplotlib reporter")

try:
    import matplotlib
except ImportError:
    raise ImproperlyConfigured("matplotlib is required to use the matplotlin reporter")

from tally.report.base import BaseReporter


class Reporter(BaseReporter):

    def __init__(self):
        pass

    def create_graph(self):
        pass
