from app.main.src.GameManagement.Models import User, Action
from app.main.src.GameManagement.Models.IModel import IModel


class Order(IModel):
    user: User
    action: Action
    amount: float
