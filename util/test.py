import os
import sys

from datetime import date
from random import randint

d = os.path.abspath(os.path.dirname(__file__))
sys.path.append("%s/.." % d)

from tally import metric


def today():
    return date(randint(2010, 2012), randint(1, 12), randint(1, 28))

from tally import backends

backends.today = today

for i in range(10000):
    metric.incr("test")
