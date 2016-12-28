from mapofinnovation.tests import *

class TestTaggingController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='tagging', action='index'))
        # Test response...
