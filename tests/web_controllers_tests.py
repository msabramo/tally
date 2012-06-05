from flaskext.testing import TestCase


class TallyControllerTest(TestCase):

    def create_app(self):

        from tally.web.controllers import app
        app.config['TESTING'] = True
        return app

    def test_home(self):
        pass
