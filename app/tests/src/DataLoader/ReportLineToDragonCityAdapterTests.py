import unittest

from app.main.src.DataLoader.Adapters import ReportLineToModelsAdapter


class ReportLineToDragonCityAdapterTests(unittest.TestCase):
    def test_adapter(self):
        result = ReportLineToModelsAdapter("21400,plankton,speed_up,50".split(','))
        self.assertEquals('21400', result.user.get_id())
        self.assertEquals('plankton', result.user.classification)
        self.assertEquals(result.user, result.game_action.user)
        self.assertEquals('speed_up', result.game_action.name)
        self.assertEquals(result.user, result.offer.user)
        self.assertEquals(result.offer.action, result.offer.action)
        self.assertEquals(50, result.offer.amount)
