

class BaseReporter(object):

    def __init__(self, backend):
        self.reporter = backend

    def create_graph(self):
        pass
