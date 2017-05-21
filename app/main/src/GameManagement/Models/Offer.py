from app.main.src.GameManagement.Models import Model, User, GameAction


class Offer(Model):
    id: str
    user: User
    action: GameAction
    amount: float
