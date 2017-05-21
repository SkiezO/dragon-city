import unittest

from app.main.src.GameManagement.Adapters import MongoAdapter
from app.main.src.GameManagement.Models import Order, User


class MongoAdapterTest(unittest.TestCase):
    def test_model_to_mongo(self):
        order = Order()
        order.user = User()
        order.user.id = 1231
        order.amount = 12123
        result = MongoAdapter.model_to_mongo(order)
        self.assertEquals(12123, result['amount'])
        self.assertEquals(1231, result['user_id'])
