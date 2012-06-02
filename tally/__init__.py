from __future__ import absolute_import

from .metric.counter import CounterManager
from .metric.record import RecordManager

counter = CounterManager()
record = RecordManager()


__all__ = ['__version__', 'counter', 'record']

__version__ = (0, 0, 1, "dev", 0)
