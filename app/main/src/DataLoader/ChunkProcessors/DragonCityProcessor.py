from app.main.src.DataLoader.ChunkProcessors import ChunkProcessor
from app.main.src.DataLoader.Adapters import ReportLineToDragonCityAdapter
from app.main.src.GameManagement.Services import UserService, ActionService, OrderService


class DragonCityProcessor(ChunkProcessor):
    user_service: UserService = UserService()
    action_service: ActionService = ActionService()
    order_service: OrderService = OrderService()

    def process_line(self, line):
        adapter_result = ReportLineToDragonCityAdapter(line.split(','))
        update_result = self.user_service.insert_or_update(adapter_result.user)
        if update_result['n'] != 1:
            raise "Cant isert update user"
            return

        adapter_result.action.id = self.action_service.insert(adapter_result.action)

        if not adapter_result.action.id:
            raise "Can't process action"
            return

        self.order_service.insert(adapter_result.order)

        return True

    def process_chunk(self, line_iterator: iter):
        for line in line_iterator:
            self.process_line(line)

