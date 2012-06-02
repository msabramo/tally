from __future__ import absolute_import

from .. import conf
from ..utils.import_tools import import_class


def get_storage(backend=None):

    if not backend:
        backend = conf.STORAGE_BACKEND

    backend_class = import_class(backend)
    return backend_class()
