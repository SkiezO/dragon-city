from app.main.src.GameManagement.Models import Model, User


class Action(Model):
    id: str
    user: User
    name: str
