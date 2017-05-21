from app.main.src.GameManagement.Models import Model, User


class GameAction(Model):
    id: str
    user: User
    name: str
