from app.main.src.GameManagement.Models import Order
from app.main.src.GameManagement.Repositories import Repository


class OrderRepository(Repository):
    def __init__(self):
        super().__init__(Order)