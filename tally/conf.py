# This could really be implemented in a much nicer way. However, it works well
# for now.

REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DATABASE = 1

STORAGE_BACKEND = 'tally.storage.backends.redis'

REPORT_BACKEND = 'tally.report.backends.matplotlib'

try:
    from tallyconfig import *
except ImportError:
    pass
