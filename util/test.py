import os
import sys

d = os.path.abspath(os.path.dirname(__file__))
sys.path.append("%s/.." % d)

from tally import metric

for i in range(1000):
    metric.incr("register")
