from app.main.src.GameManagement.Models import Order
from app.main.src.GameManagement.Repositories import OrderRepository


class OrderService:
    order_repository: OrderRepository = OrderRepository()

    def get(self, order: Order):
        return self.order_repository.get(order)
