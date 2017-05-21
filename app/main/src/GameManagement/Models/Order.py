from app.main.src.GameManagement.Models import Model, User, Action


class Order(Model):
    id: str
    user: User
    action: Action
    amount: float
