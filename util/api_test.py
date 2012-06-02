from __future__ import absolute_import

from os.path import abspath, dirname
from random import randint, choice
from sys import path
from time import time

from redis import Redis

print "HACK: Adding tally to the python path"
path.append("%s/.." % abspath(dirname(__file__)))

from tally import conf, record, counter
from tally.storage.redis import pool
from tally.web import app
from tally.metric import base


print "Flushing Redis"
redis_db = conf.REDIS_DATABASE
connection_pool = pool.get_connection_pool(db=redis_db)
conn = Redis(connection_pool=connection_pool)
conn.flushdb()

print "HACK: Monkey patching now for random dates in tally.base.now"


def now():
    now = int(time())
    year = randint(1, 60 * 2) * 30 * 24 * 7 * 52
    r = now - year
    return r

base.now = now

print "Creating dummy data points."

start = time()
stat_names = ['registrations', 'posts', 'page loads', 'updates', 'something else']
for i in xrange(10000):
    n = choice(stat_names)
    counter.incr(n)

for i in range(10000):
    record.add("Processing Time", randint(0, 5))


print "Reloaded in %f secconds....\n" % (time() - start)
print


print "KEYS :", counter.keys()
for k in counter.keys():
    print "VALS :", len(counter.values(k))


print "\n\nStarting flask web UI....\n\n"


if __name__ == "__main__":
    app.run(host="0.0.0.0", use_reloader=False)
