# This could really be implemented in a much nicer way. However, it works well
# for now.

REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DATABASE = 1

DATE_FORMAT = "%Y-%m-%d"

STORAGE_BACKEND = 'tally.backends.redis'

try:
    from tallyconfig import *
except ImportError:
    pass
