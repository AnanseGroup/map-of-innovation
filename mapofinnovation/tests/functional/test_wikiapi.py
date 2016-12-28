from mapofinnovation.tests import *

class TestWikiapiController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='wikiapi', action='index'))
        # Test response...
