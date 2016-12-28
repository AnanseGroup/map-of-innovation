from mapofinnovation.tests import *

class TestBaseapiController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='baseapi', action='index'))
        # Test response...
