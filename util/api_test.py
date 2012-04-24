from __future__ import absolute_import

from random import randint
from time import time
import os
import sys

#add tally to the path.
d = os.path.abspath(os.path.dirname(__file__))
sys.path.append("%s/.." % d)


# Monkey patch now, so we can add data on random dates.
def now():
    now = int(time())
    return randint(now - 10000, now)
from tally.storage import base
base.now = now

# Add data points.
from tally import metric
for i in xrange(100):
    metric.incr("test")


from tally import report
graph = report.create_graph("test")
graph.save("~/Desktop/test.png")
