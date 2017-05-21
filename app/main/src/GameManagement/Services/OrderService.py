from app.main.src.GameManagement.Models import Order
from app.main.src.GameManagement.Repositories import OrderRepository


class OrderService:
    order_repository: OrderRepository = OrderRepository()

    def insert(self, action: Order):
        return self.order_repository.insert(action)

    def get_by_user_id(self, user_id):
        return self.order_repository.get_by_user_id(user_id)