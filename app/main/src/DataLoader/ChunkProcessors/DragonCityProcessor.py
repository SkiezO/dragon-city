from app.main.src.DataLoader.ChunkProcessors import ChunkProcessor
from app.main.src.DataLoader.Adapters import ReportLineToDragonCityAdapter
from app.main.src.GameManagement.Services import UserService, ActionService, OrderService


class DragonCityProcessor(ChunkProcessor):
    user_service: UserService = UserService()
    action_service: ActionService = ActionService()
    order_service: OrderService = OrderService()

    def process_line(self, line):
        adapter_result = ReportLineToDragonCityAdapter(line.split(','))
        user = self.user_service.get(adapter_result.user)
        if user:
            raise "Cant find user"
            return

        adapter_result.user = user
        action = self.action_service.insert(adapter_result.action)

        if not action:
            raise "Can't process action"

        order = self.order_service.insert(adapter_result.order)

        return True

    def process_chunk(self, line_iterator: iter):
        for line in line_iterator:
            self.process_line(line)

