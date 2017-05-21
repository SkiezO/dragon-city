import unittest

from app.main.src.DataLoader.Adapters import ReportLineToMongoAdapter


class ReportLineToDragonCityAdapterTests(unittest.TestCase):
    def test_adapter(self):
        result = ReportLineToMongoAdapter("21400,plankton,speed_up,50".split(','))
        self.assertEquals('21400', result.user.get_id())
        self.assertEquals('plankton', result.user.classification)
        self.assertEquals(result.user, result.action.user)
        self.assertEquals('speed_up', result.action.name)
        self.assertEquals(result.user, result.order.user)
        self.assertEquals(result.order.action, result.order.action)
        self.assertEquals(50, result.order.amount)
