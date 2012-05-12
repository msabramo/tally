from __future__ import absolute_import

from os.path import abspath, dirname
from random import randint, choice
from sys import path
from time import time

from redis import Redis
from tally import conf
from tally import metric
from tally.storage import base
from tally.storage.backends.redis import pool
from tally.web import app

print "Adding tally to the python path"
d = abspath(dirname(__file__))
path.append("%s/.." % d)

print "Flushing Redis"
redis_db = conf.REDIS_DATABASE
connection_pool = pool.get_connection_pool(db=redis_db)
conn = Redis(connection_pool=connection_pool)
conn.flushdb()

print "Monkey patching now for random dates in tally.base.now"


def now():
    now = int(time())
    return randint(now - 100, now)
base.now = now

print "Creating dummy data points."
start = time()
for i in xrange(5000):
    n = choice(["stat1", "stat2", "stat3", "stat4"])
    metric.incr(n)

print "Reloaded in %f secconds....\n" % (time() - start)
print "Starting flask web UI....\n\n"


if __name__ == "__main__":
    app.run()
