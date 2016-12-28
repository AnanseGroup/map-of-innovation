from mapofinnovation.tests import *

class TestAdminfuncController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='adminfunc', action='index'))
        # Test response...
