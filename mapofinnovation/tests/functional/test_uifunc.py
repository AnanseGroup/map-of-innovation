from mapofinnovation.tests import *

class TestUifuncController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='uifunc', action='index'))
        # Test response...
