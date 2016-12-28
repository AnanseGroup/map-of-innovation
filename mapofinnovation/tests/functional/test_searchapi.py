from mapofinnovation.tests import *

class TestSearchapiController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='searchapi', action='index'))
        # Test response...
