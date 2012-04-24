from __future__ import absolute_import

from tally import conf
from tally.report.base import BaseReporter
from tally.metric import get_analytics
from tally.util import import_module


def importbackend(dottedpath):
    return import_module(dottedpath)


def get_backend():
    backend_path = conf.REPORT_BACKEND
    backend = importbackend(backend_path)
    return backend


def get_reporter():

    backend = get_backend()
    analytics = get_analytics()
    return BaseReporter(backend, analytics)


def create_graph(key):
    reporter = get_reporter()
    return reporter.create_graph()
