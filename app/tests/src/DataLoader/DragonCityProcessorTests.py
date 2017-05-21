import unittest

from app.main.src.DataLoader.ChunkProcessors import DragonCityProcessor
from app.main.src.GameManagement import Repository
from app.main.src.GameManagement.Models import Model
from app.main.src.GameManagement.Services import UserService, ActionService, OrderService


class DragonCityProcessorTests(unittest.TestCase):
    dragon_city_processor = DragonCityProcessor()

    def test_process_line(self):
        repository = Repository(Model)
        repository.session.drop_collection('user')
        repository.session.drop_collection('action')
        repository.session.drop_collection('order')
        self.dragon_city_processor.process_line("21400,plankton,speed_up,50")
        user_service = UserService()
        self.assertEquals('21400', user_service.get_by_id('21400')[0].id)
        action_service = ActionService()
        action = action_service.get_by_user_id('21400')[0]
        self.assertEquals('21400', action.user.id)
        self.assertEquals('speed_up', action.name)
        order_service = OrderService()
        order = order_service.get_by_user_id('21400')[0]
        self.assertEquals('21400', order.user.id)
        self.assertEquals(action.id, order.action.id)
        self.assertEquals('speed_up', order.action.name)
        self.assertEquals(50, order.amount)

